"""
    这是一个导出语雀库中所有文档的脚本, 并将文件转为md格式
"""
import json
import sys
import os
import re
import requests
import psutil
from datetime import datetime

if getattr(sys, 'frozen', False):
    APPLICATION_PATH = os.path.dirname(sys.executable)
else:
    APPLICATION_PATH = os.path.dirname('.')
jsonConfig = json.load(open(os.path.join(APPLICATION_PATH, "config.json"), encoding='utf-8'))

class ExportYueQueDoc:
    def __init__(self):
        try:
            if getattr(sys, 'frozen', False):
                APPLICATION_PATH = os.path.dirname(sys.executable)
            else:
                APPLICATION_PATH = os.path.dirname('.')
            self.jsonConfig = json.load(open(os.path.join(APPLICATION_PATH, "config.json"), encoding='utf-8'))
            self.base_url = self.jsonConfig['BASE_URL']
            self.token = self.jsonConfig['TOKEN']
            self.headers = {
                "User-Agent": self.jsonConfig['USER_AGENT'],
                "X-Auth-Token": self.jsonConfig['TOKEN']
            }
            self.data_path = self.jsonConfig['DATA_PATH']
        except:
            raise ValueError("config.json 有误")
        
    def get_user_info(self):
        """获取用户信息"""
        res_obj = requests.get(url=self.base_url + '/user', headers=self.headers)
        if res_obj.status_code != 200:
            raise ValueError("Token 信息错误")
        user_json = res_obj.json()
        self.login_id = user_json['data']['login']
        self.uid = user_json['data']['id']
        self.username = user_json['data']['name']
        print("=========== 用户信息初始化成功 ==========")
    
    def get_repos_data(self):
        """获取知识库"""
        repos_json = requests.get(self.base_url + '/users/' + self.login_id + '/repos', headers=self.headers).json()
        repos_list = []
        for item in repos_json['data']:
            rid = item['id']     # 知识库id
            name = item['name']  # 知识库名称
            repos_list.append({"rid": rid, "repos_name": name})
        return repos_list

    def get_article_data(self, repos_list):
        article_list = []
        for repos in repos_list:
            article_datas = requests.get(self.base_url + '/repos/' + str(repos['rid']) + '/docs', headers=self.headers).json()
            for item in article_datas['data']:
                bid = repos['rid']       
                title = item['title']       # 文章标题
                desc = item['description']
                slug = item['slug']
                article_list.append({"bid": bid, "title": title, "desc": desc, "slug": slug, "repos_name": repos["repos_name"]})
        
        for item in article_list:
            per_article_data = requests.get(self.base_url + '/repos/' + str(item['bid']) + '/docs/' + item['slug'],  headers=self.headers).json()
            posts_text = re.sub(r'\\n', "\n", per_article_data['data']['body'])
            result = re.sub(r'<a name="(.*)"></a>', "", posts_text)
            # all_datas.append({"title": item['title'], "content": result})
            yield result, item["repos_name"], item['title']

    def save_article(self, result, repos_name, title):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dir_path = f"{self.data_path}/{repos_name}"

        filepath = dir_path + f"/{title}.md"
        dir_ret = os.path.exists(dir_path)
        if not dir_ret:
            os.makedirs(dir_path)
        exists_ret = os.path.exists(filepath)
        if exists_ret:
            os.remove(filepath)
        try:
            with open(filepath, 'a', encoding="utf-8") as fp:
                fp.writelines(result)
            print(f"[{current_time}]  {title} 写入完成")
        except Exception as e:
            print(f"[{current_time}]  {title} 写入失败")
    
    def main(self):
        self.get_user_info()
        repos_list = self.get_repos_data()
        gen_obj = self.get_article_data(repos_list)
        for item in gen_obj:
            title = item[2].replace("\n", "").replace("<", "").replace(">", "").replace("/", "").replace("\\", "").replace("?", "").replace("|", "").replace(":", "").replace("*", "").replace('"', "")
            self.save_article(item[0], item[1], title)
    

if __name__ == "__main__":
    yq = ExportYueQueDoc()
    yq.main()