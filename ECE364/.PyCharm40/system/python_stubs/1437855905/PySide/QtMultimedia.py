# encoding: utf-8
# module PySide.QtMultimedia
# from /opt/python3/current/lib/python3.4/site-packages/PySide/QtMultimedia.so
# by generator 1.136
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QAbstractAudioDeviceInfo(__PySide_QtCore.QObject):
    # no doc
    def byteOrderList(self, *args, **kwargs): # real signature unknown
        pass

    def channelsList(self, *args, **kwargs): # real signature unknown
        pass

    def codecList(self, *args, **kwargs): # real signature unknown
        pass

    def deviceName(self, *args, **kwargs): # real signature unknown
        pass

    def frequencyList(self, *args, **kwargs): # real signature unknown
        pass

    def isFormatSupported(self, *args, **kwargs): # real signature unknown
        pass

    def nearestFormat(self, *args, **kwargs): # real signature unknown
        pass

    def preferredFormat(self, *args, **kwargs): # real signature unknown
        pass

    def sampleSizeList(self, *args, **kwargs): # real signature unknown
        pass

    def sampleTypeList(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QAbstractAudioInput(__PySide_QtCore.QObject):
    # no doc
    def bufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def bytesReady(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def notify(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def notifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def periodSize(self, *args, **kwargs): # real signature unknown
        pass

    def processedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def suspend(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QAbstractAudioOutput(__PySide_QtCore.QObject):
    # no doc
    def bufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def bytesFree(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def notify(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def notifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def periodSize(self, *args, **kwargs): # real signature unknown
        pass

    def processedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def suspend(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QAbstractVideoBuffer(__Shiboken.Object):
    # no doc
    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def handleType(self, *args, **kwargs): # real signature unknown
        pass

    def mapMode(self, *args, **kwargs): # real signature unknown
        pass

    def unmap(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    GLTextureHandle = None # (!) real value is ''
    HandleType = None # (!) real value is ''
    MapMode = None # (!) real value is ''
    NoHandle = None # (!) real value is ''
    NotMapped = None # (!) real value is ''
    ReadOnly = None # (!) real value is ''
    ReadWrite = None # (!) real value is ''
    UserHandle = None # (!) real value is ''
    WriteOnly = None # (!) real value is ''


class QAbstractVideoSurface(__PySide_QtCore.QObject):
    # no doc
    def activeChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        pass

    def isFormatSupported(self, *args, **kwargs): # real signature unknown
        pass

    def nearestFormat(self, *args, **kwargs): # real signature unknown
        pass

    def present(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def supportedFormatsChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def supportedPixelFormats(self, *args, **kwargs): # real signature unknown
        pass

    def surfaceFormat(self, *args, **kwargs): # real signature unknown
        pass

    def surfaceFormatChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Error = None # (!) real value is ''
    IncorrectFormatError = None # (!) real value is ''
    NoError = None # (!) real value is ''
    ResourceError = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    StoppedError = None # (!) real value is ''
    UnsupportedFormatError = None # (!) real value is ''


class QAudio(__Shiboken.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ActiveState = None # (!) real value is ''
    AudioInput = None # (!) real value is ''
    AudioOutput = None # (!) real value is ''
    Error = None # (!) real value is ''
    FatalError = None # (!) real value is ''
    IdleState = None # (!) real value is ''
    IOError = None # (!) real value is ''
    Mode = None # (!) real value is ''
    NoError = None # (!) real value is ''
    OpenError = None # (!) real value is ''
    State = None # (!) real value is ''
    StoppedState = None # (!) real value is ''
    SuspendedState = None # (!) real value is ''
    UnderrunError = None # (!) real value is ''


class QAudioDeviceInfo(__Shiboken.Object):
    # no doc
    def availableDevices(self, *args, **kwargs): # real signature unknown
        pass

    def defaultInputDevice(self, *args, **kwargs): # real signature unknown
        pass

    def defaultOutputDevice(self, *args, **kwargs): # real signature unknown
        pass

    def deviceName(self, *args, **kwargs): # real signature unknown
        pass

    def isFormatSupported(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def nearestFormat(self, *args, **kwargs): # real signature unknown
        pass

    def preferredFormat(self, *args, **kwargs): # real signature unknown
        pass

    def supportedByteOrders(self, *args, **kwargs): # real signature unknown
        pass

    def supportedChannels(self, *args, **kwargs): # real signature unknown
        pass

    def supportedCodecs(self, *args, **kwargs): # real signature unknown
        pass

    def supportedFrequencies(self, *args, **kwargs): # real signature unknown
        pass

    def supportedSampleSizes(self, *args, **kwargs): # real signature unknown
        pass

    def supportedSampleTypes(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QAudioEngineFactoryInterface(__PySide_QtCore.QFactoryInterface):
    # no doc
    def availableDevices(self, *args, **kwargs): # real signature unknown
        pass

    def createDeviceInfo(self, *args, **kwargs): # real signature unknown
        pass

    def createInput(self, *args, **kwargs): # real signature unknown
        pass

    def createOutput(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QAudioEnginePlugin(__PySide_QtCore.QObject, QAudioEngineFactoryInterface):
    # no doc
    def availableDevices(self, *args, **kwargs): # real signature unknown
        pass

    def createDeviceInfo(self, *args, **kwargs): # real signature unknown
        pass

    def createInput(self, *args, **kwargs): # real signature unknown
        pass

    def createOutput(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QAudioFormat(__Shiboken.Object):
    # no doc
    def byteOrder(self, *args, **kwargs): # real signature unknown
        pass

    def channels(self, *args, **kwargs): # real signature unknown
        pass

    def codec(self, *args, **kwargs): # real signature unknown
        pass

    def frequency(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def sampleSize(self, *args, **kwargs): # real signature unknown
        pass

    def sampleType(self, *args, **kwargs): # real signature unknown
        pass

    def setByteOrder(self, *args, **kwargs): # real signature unknown
        pass

    def setChannels(self, *args, **kwargs): # real signature unknown
        pass

    def setCodec(self, *args, **kwargs): # real signature unknown
        pass

    def setFrequency(self, *args, **kwargs): # real signature unknown
        pass

    def setSampleSize(self, *args, **kwargs): # real signature unknown
        pass

    def setSampleType(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    BigEndian = None # (!) real value is ''
    Endian = None # (!) real value is ''
    Float = None # (!) real value is ''
    LittleEndian = None # (!) real value is ''
    SampleType = None # (!) real value is ''
    SignedInt = None # (!) real value is ''
    Unknown = None # (!) real value is ''
    UnSignedInt = None # (!) real value is ''
    __hash__ = None


class QAudioInput(__PySide_QtCore.QObject):
    # no doc
    def bufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def bytesReady(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def notify(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def notifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def periodSize(self, *args, **kwargs): # real signature unknown
        pass

    def processedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def suspend(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QAudioOutput(__PySide_QtCore.QObject):
    # no doc
    def bufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def bytesFree(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def notify(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def notifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def periodSize(self, *args, **kwargs): # real signature unknown
        pass

    def processedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def suspend(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QVideoFrame(__Shiboken.Object):
    # no doc
    def bits(self, *args, **kwargs): # real signature unknown
        pass

    def bytesPerLine(self, *args, **kwargs): # real signature unknown
        pass

    def endTime(self, *args, **kwargs): # real signature unknown
        pass

    def fieldType(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def handleType(self, *args, **kwargs): # real signature unknown
        pass

    def height(self, *args, **kwargs): # real signature unknown
        pass

    def imageFormatFromPixelFormat(self, *args, **kwargs): # real signature unknown
        pass

    def isMapped(self, *args, **kwargs): # real signature unknown
        pass

    def isReadable(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def isWritable(self, *args, **kwargs): # real signature unknown
        pass

    def map(self, *args, **kwargs): # real signature unknown
        pass

    def mapMode(self, *args, **kwargs): # real signature unknown
        pass

    def mappedBytes(self, *args, **kwargs): # real signature unknown
        pass

    def pixelFormat(self, *args, **kwargs): # real signature unknown
        pass

    def pixelFormatFromImageFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setEndTime(self, *args, **kwargs): # real signature unknown
        pass

    def setFieldType(self, *args, **kwargs): # real signature unknown
        pass

    def setStartTime(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def startTime(self, *args, **kwargs): # real signature unknown
        pass

    def unmap(self, *args, **kwargs): # real signature unknown
        pass

    def width(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    BottomField = None # (!) real value is ''
    FieldType = None # (!) real value is ''
    Format_ARGB32 = None # (!) real value is ''
    Format_ARGB32_Premultiplied = None # (!) real value is ''
    Format_ARGB8565_Premultiplied = None # (!) real value is ''
    Format_AYUV444 = None # (!) real value is ''
    Format_AYUV444_Premultiplied = None # (!) real value is ''
    Format_BGR24 = None # (!) real value is ''
    Format_BGR32 = None # (!) real value is ''
    Format_BGR555 = None # (!) real value is ''
    Format_BGR565 = None # (!) real value is ''
    Format_BGRA32 = None # (!) real value is ''
    Format_BGRA32_Premultiplied = None # (!) real value is ''
    Format_BGRA5658_Premultiplied = None # (!) real value is ''
    Format_IMC1 = None # (!) real value is ''
    Format_IMC2 = None # (!) real value is ''
    Format_IMC3 = None # (!) real value is ''
    Format_IMC4 = None # (!) real value is ''
    Format_Invalid = None # (!) real value is ''
    Format_NV12 = None # (!) real value is ''
    Format_NV21 = None # (!) real value is ''
    Format_RGB24 = None # (!) real value is ''
    Format_RGB32 = None # (!) real value is ''
    Format_RGB555 = None # (!) real value is ''
    Format_RGB565 = None # (!) real value is ''
    Format_User = None # (!) real value is ''
    Format_UYVY = None # (!) real value is ''
    Format_Y16 = None # (!) real value is ''
    Format_Y8 = None # (!) real value is ''
    Format_YUV420P = None # (!) real value is ''
    Format_YUV444 = None # (!) real value is ''
    Format_YUYV = None # (!) real value is ''
    Format_YV12 = None # (!) real value is ''
    InterlacedFrame = None # (!) real value is ''
    PixelFormat = None # (!) real value is ''
    ProgressiveFrame = None # (!) real value is ''
    TopField = None # (!) real value is ''


class QVideoSurfaceFormat(__Shiboken.Object):
    # no doc
    def frameHeight(self, *args, **kwargs): # real signature unknown
        pass

    def frameRate(self, *args, **kwargs): # real signature unknown
        pass

    def frameSize(self, *args, **kwargs): # real signature unknown
        pass

    def frameWidth(self, *args, **kwargs): # real signature unknown
        pass

    def handleType(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def pixelAspectRatio(self, *args, **kwargs): # real signature unknown
        pass

    def pixelFormat(self, *args, **kwargs): # real signature unknown
        pass

    def property(self, *args, **kwargs): # real signature unknown
        pass

    def propertyNames(self, *args, **kwargs): # real signature unknown
        pass

    def scanLineDirection(self, *args, **kwargs): # real signature unknown
        pass

    def setFrameRate(self, *args, **kwargs): # real signature unknown
        pass

    def setFrameSize(self, *args, **kwargs): # real signature unknown
        pass

    def setPixelAspectRatio(self, *args, **kwargs): # real signature unknown
        pass

    def setProperty(self, *args, **kwargs): # real signature unknown
        pass

    def setScanLineDirection(self, *args, **kwargs): # real signature unknown
        pass

    def setViewport(self, *args, **kwargs): # real signature unknown
        pass

    def setYCbCrColorSpace(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def viewport(self, *args, **kwargs): # real signature unknown
        pass

    def yCbCrColorSpace(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    BottomToTop = None # (!) real value is ''
    Direction = None # (!) real value is ''
    TopToBottom = None # (!) real value is ''
    YCbCrColorSpace = None # (!) real value is ''
    YCbCr_BT601 = None # (!) real value is ''
    YCbCr_BT709 = None # (!) real value is ''
    YCbCr_JPEG = None # (!) real value is ''
    YCbCr_Undefined = None # (!) real value is ''
    YCbCr_xvYCC601 = None # (!) real value is ''
    YCbCr_xvYCC709 = None # (!) real value is ''
    __hash__ = None


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

