# coding=utf-8
# 上面的程式內容編碼必須在程式的第一或者第二行才會有作用

################# (1) 模組導入區
# 導入 cherrypy 模組, 為了在 OpenShift 平台上使用 cherrypy 模組, 必須透過 setup.py 安裝



import cherrypy
# 導入 Python 內建的 os 模組, 因為 os 模組為 Python 內建, 所以無需透過 setup.py 安裝
import os
# 導入 random 模組
import random
# 導入 gear 模組
#import gear

################# (2) 廣域變數設定區
# 確定程式檔案所在目錄, 在 Windows 下有最後的反斜線
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
# 設定在雲端與近端的資料儲存目錄
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    download_root_dir = os.environ['OPENSHIFT_DATA_DIR']
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
else:
    # 表示程式在近端執行
    download_root_dir = _curdir + "/local_data/"
    data_dir = _curdir + "/local_data/"


################# (3) 程式類別定義區
# 以下改用 CherryPy 網際框架程式架構
# 以下為 Hello 類別的設計內容, 其中的 object 使用, 表示 Hello 類別繼承 object 的所有特性, 包括方法與屬性設計
class Midterm(object):

    # Midterm 類別的啟動設定
    _cp_config = {
    'tools.encode.encoding': 'utf-8',
    'tools.sessions.on' : True,
    'tools.sessions.storage_type' : 'file',
    #'tools.sessions.locking' : 'explicit',
    # session 以檔案儲存, 而且位於 data_dir 下的 tmp 目錄
    'tools.sessions.storage_path' : data_dir+'/tmp',
    # session 有效時間設為 60 分鐘
    'tools.sessions.timeout' : 60
    }

    def __init__(self):
        # hope to create downloads and images directories　
        if not os.path.isdir(download_root_dir+"downloads"):
            try:
                os.makedirs(download_root_dir+"downloads")
            except:
                print("mkdir error")
        if not os.path.isdir(download_root_dir+"images"):
            try:
                os.makedirs(download_root_dir+"images")
            except:
                print("mkdir error")
        if not os.path.isdir(download_root_dir+"tmp"):
            try:
                os.makedirs(download_root_dir+"tmp")
            except:
                print("mkdir error")
    # 以 @ 開頭的 cherrypy.expose 為 decorator, 用來表示隨後的成員方法, 可以直接讓使用者以 URL 連結執行
    @cherrypy.expose
    # index 方法為 CherryPy 各類別成員方法中的內建(default)方法, 當使用者執行時未指定方法, 系統將會優先執行 index 方法
    # 有 self 的方法為類別中的成員方法, Python 程式透過此一 self 在各成員方法間傳遞物件內容
    def index(self):
        outstring = '''
        <!DOCTYPE html> 
        <html>
        <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
        </head>
        <body>
        <a href="index2">index2</a><br />
        <a href="spur2">spur2</a><br />
        <a href="drawspur2">drawspur2</a><br />
        </body>
        </html>
        '''
        
        return outstring

    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def index2(self,A=40123210, B=None):
        outstring = '''
        <!DOCTYPE html> 
        <html>
        <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
        <!-- 載入 brython.js -->
        <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
        </head>
        <!-- 啟動 brython() -->
        <body onload="brython()">
            
        <form method=POST action=index3>
        學號:<input type=text name=A value='''+str(A)+'''><br />
        姓名:<input type=text name=B value = '''+str(B)+'''><br />

        <input type=submit value=send>
        </form>
        <br /><a href="index">index</a><br />
        </body>
        </html>
        '''
        return outstring
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def index3(self,A=40123210, B=None):
        output = '''
        <!doctype html><html>
        <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
        <title>2015CD Midterm</title>
        </head> 
        <body>
        '''
        output += "學號:"+str(A)+"<br />"
        output += "姓名:"+str(B)+"<br />"
        output +='''<br /><a href="/index2">index2</a>(按下後再輸入)<br />'''
        output +='''<br /><a href="index">index</a><br />
        </body>
        </html>
        '''
        
        return output
    

        return outstring
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def spur2(self, N=20, M=5, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">
        
    <form method=POST action=spuraction>
    齒數:<input type=text name=N value='''+str(N)+'''><br />
    模數:<input type=text name=M value = '''+str(M)+'''><br />
    壓力角:<input type=text name=P value = '''+str(P)+'''><br />
    <input type=submit value=send>
    </form>
    <br /><a href="index">index</a><br />
    </body>
    </html>
    '''

        return outstring
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def spuraction(self, N=20, M=5, P=15):
        output = '''
        <!doctype html><html>
        <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
        <title>2015CD Midterm</title>
        </head> 
        <body>
        '''
        output += "齒數為"+str(N)+"<br />"
        output += "模數為"+str(M)+"<br />"
        output += "壓力角為"+str(P)+"<br />"
        output +='''<br /><a href="/spur2">spur2</a>(按下後再輸入)<br />'''
        output +='''<br /><a href="index">index</a><br />
        </body>
        </html>
        '''
        
        return output
        
        
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def drawspur(self, N=20, M=5, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    </head>
    <body>
        
    <form method=POST action=drawspuraction>
    齒數:<input type=text name=N value='''+str(N)+'''><br />
    模數:<input type=text name=M value = '''+str(M)+'''><br />
    壓力角:<input type=text name=P value = '''+str(P)+'''><br />
    <input type=submit value=畫出正齒輪輪廓>
    </form>
    <br /><a href="index">index</a><br />
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script>
    window.onload=function(){
    brython();
    }
    </script>
    </body>
    </html>
    '''

        return outstring
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def drawspuraction(self, N=20, M=5, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    </head>
    <body>
    <a href="index">index</a><br />
        
    <!-- 以下為 canvas 畫圖程式 -->
    <script type="text/python">
    # 從 browser 導入 document
    from browser import document
    from math import *
    # 請注意, 這裡導入位於 Lib/site-packages 目錄下的 spur.py 檔案
    import spur

    # 準備在 id="plotarea" 的 canvas 中繪圖
    canvas = document["plotarea"]
    ctx = canvas.getContext("2d")

    # 以下利用 spur.py 程式進行繪圖
    # N 為齒數
    N = '''+str(N)+'''
    # M 為模數
    M = '''+str(M)+'''
    # 壓力角 P 單位為角度
    P = '''+str(P)+'''
    # 計算兩齒輪的節圓半徑
    rp = N*M/2

    spur.Spur(ctx).Gear(600, 600, rp, N, P, "blue")

    </script>
    <canvas id="plotarea" width="1200" height="1200"></canvas>
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script>
    window.onload=function(){
    brython();
    }
    </script>
    </body>
    </html>
    '''

        return outstring
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def drawspur2(self, N=20,O=2, M=5, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    </head>
    <body>
        
    <form method=POST action=drawspuraction2>
    小齒輪齒數:<input type=text name=N value='''+str(N)+'''><br />
    減速比:<input type=text name=O value='''+str(O)+'''><br />
    模數:<input type=text name=M value = '''+str(M)+'''><br />
    壓力角:<input type=text name=P value = '''+str(P)+'''><br />
    <input type=submit value=畫出正齒輪輪廓>
    </form>
    <br /><a href="index">index</a><br />
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script>
    window.onload=function(){
    brython();
    }
    </script>
    </body>
    </html>
    '''

        return outstring
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def drawspuraction2(self, N=20,O=2 ,M=5, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    </head>
    <body>
    <a href="index">index</a><br />
        
    <!-- 以下為 canvas 畫圖程式 -->
    <script type="text/python">
    # 從 browser 導入 document
    from browser import document
    from math import *
    # 請注意, 這裡導入位於 Lib/site-packages 目錄下的 spur.py 檔案
    import spur

    # 準備在 id="plotarea" 的 canvas 中繪圖
    canvas = document["plotarea"]
    ctx = canvas.getContext("2d")

    # 以下利用 spur.py 程式進行繪圖
    # N 為齒數
    # 第1齒輪齒數
    n_g1 = '''+str(N)+'''
    # 第2齒輪齒數
    n_g2='''+str(O)+'''*n_g1
    # M 為模數
    m = '''+str(M)+'''
    # 壓力角 P 單位為角度
    pa = '''+str(P)+'''
    # 計算兩齒輪的節圓半徑
    rp_g1 = m*n_g1/2
    rp_g2 = m*n_g2/2

    # 繪圖第1齒輪的圓心座標
    x_g1 = 400
    y_g1 = 400
    # 第2齒輪的圓心座標, 假設排列成水平, 表示各齒輪圓心 y 座標相同
    x_g2 = x_g1 + rp_g1 + rp_g2
    y_g2 = y_g1

    # 將第1齒輪順時鐘轉 90 度
    # 使用 ctx.save() 與 ctx.restore() 以確保各齒輪以相對座標進行旋轉繪圖
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g1, y_g1)
    # rotate to engage
    ctx.rotate(pi/2)
    # put it back
    ctx.translate(-x_g1, -y_g1)
    spur.Spur(ctx).Gear(x_g1, y_g1, rp_g1, n_g1, pa, "blue")
    ctx.restore()
    # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g2, y_g2)
    # rotate to engage
    ctx.rotate(-pi/2-pi/n_g2)
    # put it back
    ctx.translate(-x_g2, -y_g2)
    spur.Spur(ctx).Gear(x_g2, y_g2, rp_g2, n_g2, pa, "black")
    ctx.restore()


    </script>
    <canvas id="plotarea" width="1200" height="1200"></canvas>
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script>
    window.onload=function(){
    brython();
    }
    </script>
    </body>
    </html>
    '''

        return outstring
    @cherrypy.expose
    # W 為正方體的邊長
    def cube(self, W=10):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    </head>
    <body>
    <!-- 使用者輸入表單的參數交由 cubeaction 方法處理 -->
    <form method=POST action=cubeaction>
    正方體邊長:<input type=text name=W value='''+str(W)+'''><br />
    <input type=submit value=送出>
    </form>
    <br /><a href="index">index</a><br />
    </body>
    </html>
    '''

        return outstring
    @cherrypy.expose
    # W 為正方體邊長, 內定值為 10
    def cubeaction(self, W=10):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 先載入 pfcUtils.js 與 wl_header.js -->
    <script type="text/javascript" src="/static/weblink/pfcUtils.js"></script>
    <script type="text/javascript" src="/static/weblink/wl_header.js">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    document.writeln ("Error loading Pro/Web.Link header!");
    </script>
    <script>
    window.onload=function(){
    brython();
    }
    </script>
    </head>
    <!-- 不要使用 body 啟動 brython() 改為 window level 啟動 -->
    <body onload="">
    <h1>Creo 參數化零件</h1>
    <a href="index">index</a><br />

    <!-- 以下為 Creo Pro/Web.Link 程式, 將 JavaScrip 改為 Brython 程式 -->

    <script type="text/python">
    from browser import document, window
    from math import *

    # 這個區域為 Brython 程式範圍, 註解必須採用 Python 格式
    # 因為 pfcIsWindows() 為原生的 JavaScript 函式, 在 Brython 中引用必須透過 window 物件
    if (!window.pfcIsWindows()) window.netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
    # 若第三輸入為 false, 表示僅載入 session, 但是不顯示
    # ret 為 model open return
    ret = document.pwl.pwlMdlOpen("cube.prt", "v:/tmp", false)
    if (!ret.Status):
        window.alert("pwlMdlOpen failed (" + ret.ErrorCode + ")")
        # 將 ProE 執行階段設為變數 session
        session = window.pfcGetProESession()
        # 在視窗中打開零件檔案, 並且顯示出來
        pro_window = session.OpenFile(pfcCreate("pfcModelDescriptor").CreateFromFileName("cube.prt"))
        solid = session.GetModel("cube.prt", window.pfcCreate("pfcModelType").MDL_PART)
        # 在 Brython 中與 Python 語法相同, 只有初值設定問題, 無需宣告變數
        # length, width, myf, myn, i, j, volume, count, d1Value, d2Value
        # 將模型檔中的 length 變數設為 javascript 中的 length 變數
        length = solid.GetParam("a1")
        # 將模型檔中的 width 變數設為 javascript 中的 width 變數
        width = solid.GetParam("a2")
        # 改變零件尺寸
        # myf=20
        # myn=20
        volume = 0
        count = 0
        try:
            # 以下採用 URL 輸入對應變數
            # createParametersFromArguments ();
            # 以下則直接利用 javascript 程式改變零件參數
            for i in range(5):
                myf ='''+str(W)+'''
                myn ='''+str(W)+''' + i*2.0
                # 設定變數值, 利用 ModelItem 中的 CreateDoubleParamValue 轉換成 Pro/Web.Link 所需要的浮點數值
                d1Value = window.pfcCreate ("MpfcModelItem").CreateDoubleParamValue(myf)
                d2Value = window.pfcCreate ("MpfcModelItem").CreateDoubleParamValue(myn)
                # 將處理好的變數值, 指定給對應的零件變數
                length.Value = d1Value
                width.Value = d2Value
                # 零件尺寸重新設定後, 呼叫 Regenerate 更新模型
                # 在 JavaScript 為 null 在 Brython 為 None
                solid.Regenerate(None)
                # 利用 GetMassProperty 取得模型的質量相關物件
                properties = solid.GetMassProperty(None)
                # volume = volume + properties.Volume
                volume = properties.Volume
                count = count + 1
                window.alert("執行第"+count+"次,零件總體積:"+volume)
                # 將零件存為新檔案
                newfile = document.pwl.pwlMdlSaveAs("cube.prt", "v:/tmp", "cube"+count+".prt")
                if (!newfile.Status):
                    window.alert("pwlMdlSaveAs failed (" + newfile.ErrorCode + ")")
                # window.alert("共執行:"+count+"次,零件總體積:"+volume)
                # window.alert("零件體積:"+properties.Volume)
                # window.alert("零件體積取整數:"+Math.round(properties.Volume));
        except:
            window.alert ("Exception occurred: "+window.pfcGetExceptionType (err))
    </script>
    '''

        return outstring
################# (4) 程式啟動區
# 配合程式檔案所在目錄設定靜態目錄或靜態檔案
application_conf = {'/static':{
        'tools.staticdir.on': True,
        # 程式執行目錄下, 必須自行建立 static 目錄
        'tools.staticdir.dir': _curdir+"/static"},
        '/downloads':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/downloads"},
        '/images':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/images"}
    }
    
root = Midterm()
#root.gear = gear.Gear()

if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示在 OpenSfhit 執行
    application = cherrypy.Application(root, config=application_conf)
else:
    # 表示在近端執行
    cherrypy.quickstart(root, config=application_conf)
