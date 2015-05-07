<!--Meta
category:公共服务
title:Deepin Bucket
DO NOT Delete Meta Above -->


## 1 概述
Deepin Bucket 主要面向Deepin用户提供公共资源存储服务，任何人都拥有Create权限。由于大多数空间采用签名认证上传的方法，Bucket将抽象出来这些空间资源的访问，并提供一个通用的REST API接口来协助上传。

根据服务器配置， 部分资源下载需要认证，这部分资源并不向普通用户开放下载，如错误日志等。

### 1.1 使用流程

Deepin Bucket 基本使用流程如下：

1 客户端向服务器申请上传资源类型。

2 服务器检查资源申请是否合法，如果合法，如果合法，则返回上传URL已经相应参数

3 客户端构造HTPP请求并进行上传

4 服务器检查上传文件的合法性


## 2 协议

对于Bucket中的每一项资源，都由唯一的ID来进行区分
/bucket/:type/
/bucket/:type/:id

POST /bucket/repoert 将创建一个资源 /bucket/repoert/1001
并且返回上次凭证，凭证有超期时间，超时凭据将失效。

GET /bucket/repoert/1001 将获得下载地址。

## 3 REST API

### 3.1 创建资源

#### 3.1.1 API EndPoint

POST https://api.linuxdeepin.com/bucket/:type/

#### 3.1.2 参数

| ParamName                  | Required      | Description                    |
| -------------------------- |---------------|------------------------------- |
| **:type**               | true          | 资源类型，目前只支持report类型，限制为大小5M以下，格式必须为gz格式。                          |


#### 3.1.3 返回结果

| ParamName      | Description         |
|--------------- |---------------------|
| **ID**        | 资源唯一标识符 |
| **ResourceUrl** | 资源访问Url |
| **PostUrl** | 资源上传Url |
| **PostHeader** | 资源上次header参数 |
| **PostBody** | 资源上传body参数 |

#### 3.1.4 示例

##### Request
```http
POST https://api.linuxdeepin.com/bucket/report
```
##### Respone
```` json
{
  "ID": "13338595ef862927186b2e485167606385ee30f1",
  "ResourceUrl": "bucket/report/13338595ef862927186b2e485167606385ee30f1",

  "PostUrl": "http://v0.api.upyun.com/theme-store",
  "PostHeader": {},
  "PostBody": {
    "policy": "eyJhbGxvdy1maWxlLXR5cGUiOiJneiIsImJ1Y2tldCI6InRoZW1lLXN0b3JlIiwiY29udGVudC1sZW5ndGgtcmFuZ2UiOiIxMDI0LDkwNDg1NzYiLCJleHBpcmF0aW9uIjoxNDI3NDQyNzUzLCJzYXZlLWtleSI6Ii9wdWJsaWMvcmVwb3J0LzIwMTUvMDMvMjcvMTUtMzctMzMtNjkxNzIxZWEuZ3oifQ==",
    "signature": "9de8e6d6d3939aaf11e79f6ed3c8b45d"
  }
}
````

### 3.2 获取资源

#### 3.2.1 API Endpoint

GET https://api.linuxdeepin.com/bucket/:type/:id

#### 3.2.2 参数
| ParamName                  | Required      | Description                    |
| -------------------------- |---------------|------------------------------- |
| **:type**               | true          | 资源类型，目前只支持report类型    |
| **:id**               | true          | 资源ID    |
| **Access-Token**     | true          | header参数， 如果资源需要认证，则必须填写该参数    |

#### 3.2.3 返回值

| ParamName      | Description         |
|--------------- |---------------------|
| **StatusCode** | 服务器将设置设置301跳转参数，直接跳转到真实下载地址 |
| ** Location** | Real Download URL |

#### 3.2.4 实例

```curl
> GET /bucket/report/c35d6cd78101da4ff586132e02090f8e3a5daf95 HTTP/1.1
> User-Agent: curl/7.35.0
> Host: api.linuxdeepin.com
> Accept: */*
>
< HTTP/1.1 301 Moved Permanently
* Server nginx/1.0.11 is not blacklisted
< Server: nginx/1.0.11
< Date: Fri, 27 Mar 2015 07:55:18 GMT
< Content-Type: text/plain; charset=utf-8
< Connection: keep-alive
< Location: http://theme-store.b0.upaiyun.com/public/report/2015/03/27/15-52-39-fff3f103.gz
< Content-Length: 0
< * Connection #0 to host api.linuxdeepin.com left intact
```

## 4 SDK

### 4.1 Python

直接调用postfile函数上传文件， 访问地址保存在ResourceUrl中。

```python
import json
import requests
from collections import namedtuple

BucketHost = "https://api.linuxdeepin.com/"
BucketApi = "https://api.linuxdeepin.com/bucket/"

'''
Credential
{
  "ID": "510c22ca9564368c52c08e828c1",
  "ResourceUrl": "bucket/report/510c22ca9564368c52c08e828c1",

  "PostUrl": "http://v0.api.upyun.com/theme-store",
  "PostHeader": {},
  "PostBody": {
    "policy": "eyJhbGxvdy1maWxlLXR5c==",
    "signature": "e6fa7aaaec6c43f28888e9fd14e1de72"
  }
}
'''
def json2Credential(data):
    return json.loads(data, object_hook=lambda d: namedtuple('Credential', d.keys())(*d.values()))

def postfile(restype, filepath):
    # require a post credential
    url = BucketApi + restype
    r = requests.post(url)
    cre = json2Credential(r.text)

    files= {"file": ("file.tar.gz", open(filepath, 'rb'))}
    fr = requests.post(cre.PostUrl, files=files,data=cre.PostBody.__dict__, headers=cre.PostHeader)
    if 200 == fr.status_code:
        return cre
    print(fr.text)
    return fr.status_code

if __name__=="__main__":
    filename="testdata.tar.gz"
    restype = "report"
    cre = postfile(restype, filename)
    print("File ID:", cre.ID)
    print("File Url:", BucketHost+cre.ResourceUrl)

```

### 4.2 Perl

调用 uploadReportAttachment 函数上传报告附件

```perl
#!/usr/bin/env perl
use 5.018;
use warnings;
use utf8;

use Data::Dumper;
use LWP::UserAgent;
use HTTP::Request::Common;
use JSON qw(decode_json);

my $ua = LWP::UserAgent->new;
$ua->timeout(10);
my $deepin_api = "https://api.deepin.org";

sub uploadReportAttachment
{
	my ($file_path) = @_;
	my $url = "$deepin_api/bucket/report";
	my $res = $ua->post($url);
	if ($res->is_success)
	{
		my $credential = decode_json($res->content);
		print "Credential = ", Dumper $credential;
		my $response = $ua->request(POST $credential->{PostUrl},
			Content_Type => 'multipart/form-data',
			%{ $credential->{PostHeader} },
			Content => [
				%{ $credential->{PostBody} },
				file => [ $file_path ]
			]
		);

		if ($response->is_success )
		{
			say $response->content;
			say "url is $deepin_api/". $credential->{ResourceUrl};
		}
		else
		{
			die $response->status_line, $response->content;
		}
	}
	else
	{
		die $res->status_line, $res->content;
	}
}


uploadReportAttachment("./testdata.tar.gz");


```
