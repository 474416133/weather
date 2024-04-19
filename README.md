# Readme

### 1 目的 

> 做一个国内各大城市的天气查询工具，分别提供数据接口和界面显示
>
> 数据源来自 http://v1.yiketianqi.com

### 2 完成列表  

- [x]  城市天气查询接口 
- [x] 界面 
- [ ] swagger 接口文档

### 3 使用的技术 

- [x] python 3.11

- [x] flask 
- [x] bootstrap
- [x] jinja2

### 4 开发相关  

#### 4.1 获取代码 

```
git clone ....   
# 创建虚拟环境
cd weather 
pip install -r requirements/dev.txt
```



#### 4.2 代码目录说明 

```
├─app
│  ├─.env                    # 项目配置
│  ├─blueprints              
│  │  ├─api                  # 接口
│  │  ├─page                 # 页面
│  ├─common                  # 公共类库
│  ├─managers                # 数据操作管理类
│  ├─models                  # 数据模型
├─docker
├─logs                       # 日志
├─requirements               # 项目依赖库
├─static                     # 项目静态资源
├─templates                  # 页面模板
├─tests                      # 项目测试
```



#### 4.3 运行项目  

```
# 在虚拟环境中
cd weather 
python main.py
```



### 5 部署相关 

#### 5.1 生成docker镜像 

#### 5.2 uwsgi.ini配置

#### 5.3 docker run 命令

#### 5.4 ssl与nginx的配置





