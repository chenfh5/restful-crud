# restful-crud
> based on [django-rest-framework](https://www.django-rest-framework.org/tutorial/quickstart/) and IDEA to make a demo

## QuickStart
- git clone
- cd restfulcrud/rdemo
- open `CMD`
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver localhost:8000
- Enter Your `URL`, e.g., `test cmd`

## test cmd
|Type|URL|Description|
|---|---|---|
|`C`|http://localhost:8000/person/create1/?name=c1&phone=13800138000&age=11&address=cn|||
|C|http://localhost:8000/person/create1/?name=c2&phone=123 |这里限定phone 11位失败，原因待查|
|C|http://localhost:8000/person/create1/?name=c3&phone=123&age=11&address=en||
|C|http://localhost:8000/person/create1/?name=c4&phone=123&age=11&address=us||
|C|http://localhost:8000/person/create1/?name=c5&phone=123&age=11&address=cn||
|C|http://localhost:8000/person/create1/?name=c6&phone=123&age=12&address=eu||
|`R`|http://localhost:8000/person/retrieve1|将展示全部record|
|R|http://localhost:8000/person/retrieve1/?phone=13800138000|将展示特定phone的record|
|R|http://localhost:8000/person/retrieve1/?age=2|将展示age>=2的record|
|R|http://localhost:8000/person/retrieve1/?address=e|将展示address带有e的record|
|`U`|http://localhost:8000/person/update1/?name=c2&phone=123&age=99|将修改其年龄到99|
|U|http://localhost:8000/person/update1/?name=c3&phone=123&address=中国|将修改其年龄到99|
|U|http://localhost:8000/person/update1/?name=c4&phone=123&age=101&address=中国|将修改其年龄到99|
|`D`|http://localhost:8000/person/destroy1|将删除全部record|
|D|http://localhost:8000/person/destroy1/?name=c3|将删除名字是c3的record|
|D|http://localhost:8000/person/destroy1/?age=11|将删除名字是c3的record|
|D|http://localhost:8000/person/destroy1/?name=c6&age=12|将删除名字是c6且其年龄是11的record|

## Reference
- [Django REST framework](https://www.django-rest-framework.org/)
- [CN doc](https://www.jianshu.com/p/97c326198fb3)