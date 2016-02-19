<!--Meta
category:参考文档
title:下载接口
DO NOT Delete Meta Above -->

## 1.介绍
深度下载服务分为transfer和download-service两个接口，tranfser针对单个链接任务提供下载服务，download-service则提供管理一组链接下载管理功能。
其对应dbus接口分别为com.deepin.api.Transfer和com.deepin.download.service

## 2. com.deepin.api.Transfer

### 2.1 方法

#### 2.1.1 Download

     Download(url string, localfile string, md5 string, ondup int32) (retCode int32, taskid string)
     
     添加一个下载任务

     url: 下载地址
     localfile: 本地文件路径
     md5: 文件hash，如果没有则留空
     ondup: 是否覆盖同名文件 
         ondup=64: 重命名
         ondup=65: 覆盖

    retCode: 返回值 0成功， 其他表示添加任务失败
    taskid: tranfer任务id

#### 2.1.2 Pause
    
    Pause（taskid string）

    暂停任务

#### 2.1.3 Resume

    Resume（taskid string）

    恢复暂停的任务

#### 2.1.4 Cancel
    
    Cancel（taskid string）

    停止/取消任务，停止任务后，任务会被删除

#### 2.1.5 QuerySize

    QuerySize(url string)

    查询服务器返回的Content-Length值，如果服务器支持该方法，则返回0


#### 2.1.6 TransferCount

    TransferCount()

    返回全部任务数目

#### 2.1.7 ListTransfer

    ListTransfer()

    列出所有任务的认为id
    

#### 2.1.8 GetTransfer

    GetTransfer（taskid string）

    查询任务信息

返回值示例:

````
Taskid: b6f0485e-8893-4346-af6f-1f09550e6fc7_transfer
Status: 16
Url: http://packages.linuxdeepin.com/deepin/pool/universe/g/google-chrome-beta/google-chrome-beta_43.0.2357.37-1_amd64.deb
MD5: a01c724f4240fe49890290067c167f1b
OnDup: 65
FileSize: 48031000
FileName: 
LocalFile: /var/cache/apt/archives/google-chrome-beta_43.0.2357.37-1_amd64.deb
StatusFile: /var/cache/apt/archives/google-chrome-beta_43.0.2357.37-1_amd64.deb.tfst
DownLoadSize: 29368542
TotalSize: 48031000
````

### 2.2 信号

    信号1s发生一次

#### 2.1.1 ProcessReport
  
    ProcessReport func(taskid string, detaBytes int64, finishBytes int64, totalBytes int64)                                                                           

    任务下载进度

    taskid: 任务id
    detaByte: 相对上次汇报新增下载量
    finishBytes: 下载完成的字节数
    totalBytes: 文件总大小，为0表示大小未知

#### 2.1.2 FinishReport 

    FinishReport  func(taskid string, statusCode int32)    

    任务完成信号    

    taskid: 任务id
    statusCode: 任务状态,可能为如下值:

        TaskStart   = int32(0x10)
        TaskSuccess = int32(0x11)
        TaskFailed  = int32(0x12)
        TaskNoExist = int32(0x13)
        TaskPause   = int32(0x14)
        TaskCancel  = int32(0x15)

## 3. com.deepin.download.service

### 3.1 方法

#### 3.1.1 AddTask

    AddTask(taskName string, urls []string, sizes []int64, md5s []string, storeDir string) (taskid string)

    添加下载任务到下载队列中

    taskname:   任务名称
    urls:       下载的地址列表
    sizes:      下载文件大小列表（在服务器无法获取大小时生效，若能从服务器获得文件大小，则忽略该属性）
    md5s:       下载文件MD5列表（若不为空，则下载完成后会验证md5）
    storeDir:   存储位置
    taskid:     返回用于标示本次下载的任务id

#### 3.1.2 PauseTask
    
    PauseTask（taskid string）

    暂停任务

#### 3.1.3 ResumeTask

    ResumeTask（taskid string）

    恢复暂停的任务

#### 3.1.4 SoptTask
    
    SoptTask（taskid string）

    停止/取消任务，停止任务后，任务会被删除

### 3.2 信号

#### 3.2.1 Wait 
    
    Wait func(taskid string)

	任务下载未开始,处于等待准备状态时发出

	taskid: 任务id

#### 3.2.2 Start

    Start func(taskid string)

	任务下载开始时发出

	taskid: 任务id

#### 3.2.3 Update

    Update func(taskid string, progress int32, speed int32, finish int32, total int32, downloadSize int64, taotalSize int64)

    每秒钟针对每个任务发出一个更新信号

    taskid: 任务id
    process: 下载进度0~100
    speeds 下载速度 Bit/s
    finish 下载完成的url数目
    total  总共下载的url数目
    downloadSize 已经下载的数据 Byte
    totalSize 总共需要下载的数据 Byte

#### 3.2.4 Finish

    Finish func(taskid string)

	任务完成时发出

#### 3.2.5 Stop

    Stop func(taskid string)

	任务停止时发出, 任务Stop后会被立即删除，无法再获得任务信息，
	一般发出Stop信号，则任务任务失败

	taskid: 任务id

#### 3.2.6 Pause

    Pause func(taskid string)

	任务暂停时发出

	taskid: 任务id

#### 3.2.7 Resume

    Resume func(taskid string)

	任务继续时发出

	taskid: 任务id

#### 3.2.8 Error

    Error func(taskid string, errcode int32, errstr string)

	发生错误时发出

	taskid: 任务id, 为空时表示与下载无关错误
	errcode: 错误码
	errStr: 错误描述

