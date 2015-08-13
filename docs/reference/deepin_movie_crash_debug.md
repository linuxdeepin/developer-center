<!--Meta
category:参考文档
title:调试与定位Bug方法与技巧分享 --- 深度影院崩溃解决过程
DO NOT Delete Meta Above -->
## 调试与定位Bug方法与技巧分享

公司在Tower上给我派了一个任务，让我讲一下调试与定位Bug的方法和技巧， 演讲我不擅长，就先把我的一些经验和体会写一个Wiki吧.

### 方法大家都应该用过了:

1.  阅读源码:可以知道是否需要了解一些专业背景知识;可以看到是否有简单的逻辑错误;
2.  打日志:对可疑的地方和不理解的地方<**勤快**>加日志，运行程序后认真分析日志，知道程序的更多行为;
3.  使用调试器:
    *   对关键函数加一个断点，查看堆栈一下子就知道这个函数的调用流程;
    *   对关键变量加内存读写断点, 一下子就知道什么时候什么地方访问和修改了这个变量;
    *   熟悉更多的[调试器命令](http://www.cs.berkeley.edu/~mavam/teaching/cs161-sp11/gdb-refcard.pdf), 节省时间;

### 技巧我觉得是一个内心修炼的过程:

1.  不怕困难, 坚信自己一定可以找到bug并修复它;
2.  不急躁,不时用笔和纸记下一些敏感数据,调整分析目标;
3.  不贪心，有的bug要花上几天才可以解决，只要每天有收获就是进步;
4.  不纠结, 针对问题选择一个合适的调试方法就可以,有时候最简单的方法就是最快的方法;

### Bug实例: 深度影院切换声道程序崩溃

1.  打开深度影院，播放一个视频;
2.  播放过程中,在视频画面鼠标右键,打开右键菜单;
3.  声音->Audio Channels->Stereo/Left/Right，来回切换Stereo/Left/Right;
4.  深度影院崩溃.

***********************************************************

### 下面是我解决过程回顾,希望可以给大家一些提示

***********************************************************

#### 先用调试器看崩溃的时候堆栈,获取更多信息

*   gdb --pid=xxx, xxx是深度影院的进程，这里就是python的进程id.

    <pre>Program received signal SIGABRT, Aborted.
    [Switching to Thread 0x7fa6c9a3a700 (LWP 32018)]
    0x00007fa72a979cc9 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
    56	../nptl/sysdeps/unix/sysv/linux/raise.c: 没有那个文件或目录.
    (gdb) bt
    #0  0x00007fa72a979cc9 in __GI_raise (sig=sig@entry=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
    #1  0x00007fa72a97d0d8 in __GI_abort () at abort.c:89
    #2  0x00007fa72a9b6394 in __libc_message (do_abort=do_abort@entry=1, fmt=fmt@entry=0x7fa72aac4b28 "*** Error in `%s': %s: 0x%s ***\n")
        at ../sysdeps/posix/libc_fatal.c:175
    #3  0x00007fa72a9c10f7 in malloc_printerr (action=<optimized out>, str=0x7fa72aac0d1d "realloc(): invalid next size", ptr=<optimized out>) at malloc.c:4996
    #4  0x00007fa72a9c4937 in _int_realloc (av=<optimized out>, oldp=0x7fa6bc00bfe0, oldsize=<optimized out>, nb=<optimized out>) at malloc.c:4234
    #5  0x00007fa72a9c5fc9 in __GI___libc_realloc (oldmem=0x7fa6bc00bff0, bytes=64) at malloc.c:3029
    #6  0x00007fa728e81fad in QByteArray::reallocData(unsigned int, QFlags<QArrayData::AllocationOption>) () from /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
    #7  0x00007fa728e821c4 in QByteArray::resize(int) () from /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
    #8  0x00007fa729104a66 in ?? () from /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
    #9  0x00007fa729104da1 in ?? () from /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
    #10 0x00007fa728f19b0d in QString::toLocal8Bit_helper(QChar const*, int) () from /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
    #11 0x00007fa728e70d73 in ?? () from /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
    #12 0x00007fa728e6ea6e in qt_message_output(QtMsgType, QMessageLogContext const&, QString const&) () from /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
    #13 0x00007fa6f3c8fc89 in QDebug::~QDebug (this=0x7fa6c9a398e0, __in_chrg=<optimized out>) at /usr/include/x86_64-linux-gnu/qt5/QtCore/qdebug.h:89
    #14 0x00007fa6f3cd470a in QtAV::Internal::log_helper(QtMsgType, const QMessageLogger *, const char *, typedef __va_list_tag __va_list_tag *) (
        msgType=QtWarningMsg, qlog=0x7fa6c9a39b20, msg=0x7fa6f3d74cfb "[AudioResamplerFF end] %d", ap=0x7fa6c9a39988)
        at /home/frank/hackday/QtAV/src/utils/Logger.cpp:58
    #15 0x00007fa6f3cd4a9f in QtAV::Internal::Logger::warning (this=0x7fa6c9a39b20, msg=0x7fa6f3d74cfb "[AudioResamplerFF end] %d")
        at /home/frank/hackday/QtAV/src/utils/Logger.cpp:100
    #16 0x00007fa6f3c8c416 in QtAV::AudioResamplerLibav::convert (this=0x76f2f00, data=0x7fa6bc005f08)
        at /home/frank/hackday/QtAV/src/AudioResamplerTemplate.cpp:115
    #17 0x00007fa6f3ce29ff in QtAV::AudioFrame::to (this=0x7fa6c9a39e20, fmt=...) at /home/frank/hackday/QtAV/src/AudioFrame.cpp:226
    #18 0x00007fa6f3cd6cda in QtAV::AudioThread::run (this=0x71f5560) at /home/frank/hackday/QtAV/src/AudioThread.cpp:250
    #19 0x00007fa728e7ea5f in ?? () from /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
    #20 0x00007fa72ad10182 in start_thread (arg=0x7fa6c9a3a700) at pthread_create.c:312
    #21 0x00007fa72aa3d47d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:111
    </pre>

    从堆栈看崩溃是glibc的realloc函数调用了abort终止了进程,但实际来看不可能是glibc的错误.

*   同时在终端里面看到:深度影院输出了这样一条信息:

    <pre>*** Error in `python': realloc(): invalid next size: 0x00007fa6bc00bff0 ***
    </pre>

    上网查找"realloc(): invalid next size"，原因看起来是glibc前一次分配的内存有破坏. 导致后续的realloc,alloc,free函数在检查内部维护的内存块表的时候发现了错误就调用abort终止了进程， 维基百科把这类情况叫[memory corruption](https://en.wikipedia.org/wiki/Memory_corruption); 所以还得看深度影院的源码，搞清楚处理逻辑,才能知道是哪个地方破坏了内存.

#### 由于切换声道导致的崩溃，先查找声音处理的代码在哪里?

*   在界面源码目录: git grep "Audio Channels" (用"left", "right"有很多结果，所以用"Audio Channels") src/controllers/menu_controller.py: ("_audio_channel", _("Audio Channels")), 打开src/controllers/menu_controller.py,看到这样的代码:

    <pre>self.audioChannelChanged.emit("left")
    self.audioChannelChanged.emit("right")
    self.audioChannelChanged.emit("stereo")
    audioChannelChanged = pyqtSignal(str, arguments=["channelLayout"])
    </pre>

*   git grep "channelLayout"

    <pre>src/controllers/MenuResponder.qml:    onAudioChannelChanged: { main_controller.setAudioChannel(channelLayout) }
    src/controllers/menu_controller.py:    audioChannelChanged = pyqtSignal(str, arguments=["channelLayout"])
    src/views/MainController.qml:    function setAudioChannel(channelLayout) {
    src/views/MainController.qml:   console.log(channelLayout);
    src/views/MainController.qml:        switch(channelLayout) {
    src/views/MainController.qml:                player.channelLayout = MediaPlayer.Left
    src/views/MainController.qml:                player.channelLayout = MediaPlayer.Right
    src/views/MainController.qml:                player.channelLayout = MediaPlayer.Stero
    </pre>

*   打开src/views/MainController.qml, 看到这样的代码:

    <pre>import QtAV 1.6
    </pre>

*   到QtAV源码目录, 再一次 git grep "channelLayout"

    <pre>qml/QmlAV/QmlAVPlayer.h:    Q_PROPERTY(ChannelLayout channelLayout READ channelLayout WRITE setChannelLayout NOTIFY channelLayoutChanged)
    qml/QmlAV/QmlAVPlayer.h:    ChannelLayout channelLayout() const;
    qml/QmlAV/QmlAVPlayer.h:    void channelLayoutChanged();
    qml/QmlAVPlayer.cpp:    connect(this, SIGNAL(channelLayoutChanged()), SLOT(applyChannelLayout()));
    qml/QmlAVPlayer.cpp:    emit channelLayoutChanged();
    qml/QmlAVPlayer.cpp:QmlAVPlayer::ChannelLayout QmlAVPlayer::channelLayout() const
    qml/QmlAVPlayer.cpp:    AudioFormat::ChannelLayout ch = toAudioFormatChannelLayout(channelLayout());
    qml/QmlAVPlayer.cpp:    if (channelLayout() == ChannelLayoutAuto || ch == af.channelLayout())
    </pre>

    打开qml/QmlAVPlayer.cpp,找到界面切换声道处理函数: void QmlAVPlayer::applyChannelLayout() 跟进去最终截止在这个函数:void AudioOutput::setAudioFormat(const AudioFormat& format)

*   git grep "audioFormat" 看怎么用的?，过滤掉搜索结果后，这几个地方是比较可疑的:

    <pre>src/AudioThread.cpp:                    || dec->resampler()->outAudioFormat() != ao->audioFormat()) {
    src/AudioThread.cpp:                    qDebug() << "ao.format " << ao->audioFormat();
    src/AudioThread.cpp:                    dec->resampler()->setOutAudioFormat(ao->audioFormat());
    src/AudioThread.cpp:            //if (ao->audioFormat() != frame.format()) {
    src/AudioThread.cpp:                frame = frame.to(ao->audioFormat());
    </pre>

    打开src/AudioThread.cpp,找到frame.to，跟进去来到

    <pre>AudioFrame AudioFrame::to(const AudioFormat &fmt) const
    </pre>

    最终可以看到声音是在这个函数进行转换处理的:

    <pre>bool AudioResamplerFF::convert(const quint8 **data)
    </pre>

*   在调试器里面单步调试这个convert函数，除了这一行swr_convert函数是一个第三方库函数，没有源码:

    <pre>int converted_samplers_per_channel = swr_convert(d.context, out, d.out_samples_per_channel, data, d.in_samples_per_channel);
    </pre>

    都比较正常,对这一行前后加日志:

    <pre>    qWarning("[AudioResamplerFF begin] speed=%.2f,%p,%d,%d,%d,%d->%p,%d,%d,%d,%d", d.speed,
                out, d.out_samples_per_channel, d.out_format.sampleRate(), d.out_format.sampleFormatFFmpeg(), d.out_format.channelLayout(),
                data, d.in_samples_per_channel, d.in_format.sampleRate(), d.in_format.sampleFormatFFmpeg(), d.in_format.channelLayout());
        int converted_samplers_per_channel = swr_convert(d.context, out, d.out_samples_per_channel, data, d.in_samples_per_channel);
        qWarning("[AudioResamplerFF end] %d", converted_samplers_per_channel);

    </pre>

    观察切换声道时候的日志情况,立体声时候:

    <pre>"[AudioResamplerFF begin]
    speed=1.00,0x7f908bffdaf0,2176,44100,8196,3->0x7f907c005ee8,2048,44100,40964,3"
    "[AudioResamplerFF end] 2048"
    </pre>

    切换到左声道后,channelLayout变化了:

    <pre>"[AudioResamplerFF begin]
    speed=1.00,0x7f908bffdaf0,2176,44100,8196,0->0x7f907c006788,2048,44100,40964,3"
    "[AudioResamplerFF end] 2048"
    </pre>

*   尝试把converted_samplers_per_channel=swr_convert改成converted_samplers_per_channel=2048， 编译一个新的QtAV，发现不管怎么切换声道后不崩溃了,所以原因就是传给swr_convert的内存buffer不够.

*   继续阅读源码，查找d.context的创建情况，发现是这个函数bool AudioResamplerFF::prepare()里面创建的. 经王耀华指导，知道王斌是QtAV的作者，也是我们的上海同事, 所以跟王斌咨询了一下:

    <pre>汉_WINE_刘昌辉刘昌辉15:07
    hi,我想问一下，这个函数AudioResamplerFF::prepare()
    是不是每次改变audio format时候都要调用一下。

    沪_开发_王斌王斌15:07
    对

    汉_WINE_刘昌辉刘昌辉15:08
    比如切换声道的时候：切换声道的时候:
    #0 QtAV::AudioOutput::setAudioFormat (this=0x3ee2080, format=...) at
    /home/frank/hackday/QtAV/src/output/audio/AudioOutput.cpp:445
    这个函数怎么调用AudioResamplerFF::prepare()？
    我对AudioResamplerFF::prepare()加断点，发现在调用QtAV::AudioOutput::setAudioFormat (this=0x3ee2080, format=...) at
    /home/frank/hackday/QtAV/src/output/audio/AudioOutput.cpp:445之后，没有触发AduioResamplerFF::prepare函数调用。

    沪_开发_王斌王斌15:10
    这个不会调用，只有在解码后发现音频数据和音频设备支持的格式不一致的时候才会

    汉_WINE_刘昌辉刘昌辉15:12
    但是比如原来是立体声，我在界面设置成左声道后，应该要调用AduioResamplerFF::prepare吧，但是断点也没有触发。

    沪_开发_王斌王斌15:14
    应该会调用的，我看看

    汉_WINE_刘昌辉刘昌辉15:16
    在audioframe.cpp有这3个注释： conv->setInAudioFormat(format());
    conv->setOutAudioFormat(fmt);
    //conv->prepare(); // already called in setIn/OutFormat
    我感觉不能去掉//
    或者要在这样做：
    void AudioResampler::setOutAudioFormat(const AudioFormat& format)
    {
    d_func().out_format = format;
    + prepare();
    }

    沪_开发_王斌王斌15:18
    咦，好像是额，设置输出格式后没有prepare

    沪_开发_王斌王斌15:18
    对
    </pre>

### 已经确认是内存错误，使用大杀器: valgrind 看看

注:这个方法我hackday那天一开始试过了，但是在valgrind程序没有崩溃，所以hackday那天就放弃了这个方法; 提交了补丁后,考虑到这种内存问题是很普遍的问题,不甘心又尝试了一次valgrind的，发现valgrind确实非常有用. 推荐大家在遇到内存问题的时候使用,一定要认真分析valgrid的输出报告.

*   在这里下载: [http://valgrind.org/downloads/valgrind-3.10.1.tar.bz2](http://valgrind.org/downloads/valgrind-3.10.1.tar.bz2)

*   编译安装 valgrind:

    <pre>    ./configure && sudo make install
    </pre>

*   先重新编译QtAV,生成调试符号，详细见附录1;然后在valgrind里面运行深度影院:

    <pre>  valgrind -v --log-file=~/mem.log python src/main.py 
    </pre>

*   由于在valgrind里面程序没有崩溃，所以只要切换一下声道后就退出程序; 然后打开mem.log, 搜索一些内存错误的关键字，比如"Invalid write of size", 或者目标可疑模块名称，比如QtAV, libavresample.so等, 非常给力的看到了如下日志：

    <pre>==24846== Thread 16 QtAV::AudioThread:
    ==24846== Invalid write of size 4
    ==24846==    at 0x2A8C0228: ??? (in /usr/lib/x86_64-linux-gnu/libavresample.so.1.0.1)
    ==24846==    by 0x2A8C22AD: ??? (in /usr/lib/x86_64-linux-gnu/libavresample.so.1.0.1)
    ==24846==    by 0x2A8C82D1: avresample_convert (in /usr/lib/x86_64-linux-gnu/libavresample.so.1.0.1)
    ==24846==    by 0x2A54897B: QtAV::AudioResamplerLibav::convert(unsigned char const**) (AudioResamplerTemplate.cpp:111)
    ==24846==    by 0x2A59F1F6: QtAV::AudioFrame::to(QtAV::AudioFormat const&) const (AudioFrame.cpp:226)
    ==24846==    by 0x2A5934AB: QtAV::AudioThread::run() (AudioThread.cpp:250)
    ==24846==    by 0x6CF2A5E: ??? (in /usr/lib/x86_64-linux-gnu/libQt5Core.so.5.3.1)
    ==24846==    by 0x4E3E181: start_thread (pthread_create.c:312)
    ==24846==    by 0x514E47C: clone (clone.S:111)
    ==24846==  Address 0x32a64ff0 is 0 bytes after a block of size 16,384 alloc'd
    ==24846==    at 0x4C2CB0A: realloc (vg_replace_malloc.c:692)
    ==24846==    by 0x6CF5FAC: QByteArray::reallocData(unsigned int, QFlags<QArrayData::AllocationOption>) (in /usr/lib/x86_64-linux-gnu/libQt5Core.so.5.3.1)
    ==24846==    by 0x6CF61C3: QByteArray::resize(int) (in /usr/lib/x86_64-linux-gnu/libQt5Core.so.5.3.1)
    ==24846==    by 0x2A548A47: QtAV::AudioResamplerLibav::convert(unsigned char const**) (AudioResamplerTemplate.cpp:121)
    ==24846==    by 0x2A59F1F6: QtAV::AudioFrame::to(QtAV::AudioFormat const&) const (AudioFrame.cpp:226)
    ==24846==    by 0x2A5934AB: QtAV::AudioThread::run() (AudioThread.cpp:250)
    ==24846==    by 0x6CF2A5E: ??? (in /usr/lib/x86_64-linux-gnu/libQt5Core.so.5.3.1)
    ==24846==    by 0x4E3E181: start_thread (pthread_create.c:312)
    ==24846==    by 0x514E47C: clone (clone.S:111)
    ==24846==
    </pre>

    日志的左边起的第一列是进程pid,第二列是发现内存错误时候的调用堆栈;日志的这一行, 正是程序崩溃的罪魁祸首:

    <pre>==24846==    by 0x2A8C82D1: avresample_convert (in /usr/lib/x86_64-linux-gnu/libavresample.so.1.0.1)
    </pre>

### 附录1: QtAV源码编译方法:

1.  git clone [http://gitcafe.com/Deepin/QtAV.git](http://gitcafe.com/Deepin/QtAV.git)
2.  安装编译依赖: sudo apt-get build-dep libqtav
3.  新建一个干净的build目录: rm -rf build && mkdir build && cd build
4.  配置makefile: qmake QMAKE_CXXFLAGS+="-g -O0 -fno-inline -fno-omit-frame-pointer" QMAKE_CFLAGS+="-g -O0 -fno-inline -fno-omit-frame-pointer" CONFIG+=debug ..
5.  编译: make -j4
6.  安装: sudo ./sdk_install.sh

### 附录2: deepin-qml-widgets 安装

1.  git clone [http://gitcafe.com/Deepin/deepin-qml-widgets.git](http://gitcafe.com/Deepin/deepin-qml-widgets.git)
2.  安装编译依赖: sudo apt-get build-dep deepin-qml-widgets
3.  编译安装: sudo ./rebuild.sh

### 附录3: deepin-movie启动方法

1.  git clone [http://gitcafe.com/Deepin/deepin-movie.git](http://gitcafe.com/Deepin/deepin-movie.git)
2.  sudo cp bin/* /usr/bin
3.  启动deepin-movie: python src/main.py 或者开启日志方式 QTAV_LOG_LEVEL=all python src/main.py
