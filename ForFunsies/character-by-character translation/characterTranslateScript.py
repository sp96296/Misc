# follow https://cloud.google.com/translate/docs/reference/libraries#client-libraries-install-python
# and maybe https://cloud.google.com/translate/docs/quickstart-client-libraries
from google.cloud import translate
import csv

OUTPUT_LANGUAGE = "en"
OUTPUT_LANGUAGE_RANGE_LIST = list(range(65,91)) + list(range(97,123))
FILE_OUT_TXT = "translated.txt"
FILE_OUT_CSV = "translated.csv"


# rn it's formatted to work on single char words 
def strToSingleCharacterList(string):
    strList = []
    for character in string:
        strList.append(character)
    return strList

def checkTranslated(client, char, originalLang):
    translation = char
    detectedDetails = client.detect_language(char)
    detectedLang = detectedDetails["language"]
    if detectedLang == originalLang:
        correction = "Attempting to correct {} from {} to {}".format(char, detectedLang, OUTPUT_LANGUAGE)
        print(correction)
        result = translateItem(client, char)
        translation = result["translated"]
    return translation
        

def translateItem(client, item):
    values = {}
    translatedResult = client.translate(item, target_language=OUTPUT_LANGUAGE)
    values["detectedLang"] = translatedResult["detectedSourceLanguage"]
    values["translated"] = translatedResult["translatedText"]
    return values

def translateFromList(details):
    client, strList= details
    translatedDict = {}
    for item in strList:
        whitespace = [' ', '\n', '\r', '\t', '\f', '\v']
        if (item not in whitespace):
            values = translateItem(client, item)
            translated, detectedLang = values["translated"], values["detectedLang"]
            checked = checkTranslated(client, translated, detectedLang)
            translatedDict[item] = checked
            strDetails = [item, checked]
            prettyPrint(strDetails)
    return translatedDict

def prettyPrint(item):
    key = item[0]
    value = item[1]
    formatted = "{} | {}".format(key, value)
    print(formatted)

def saveToFile(dictionary):
    keys = dictionary.keys()
    with open(FILE_OUT_TXT, "w+", encoding='utf-8') as file:
        data = file.readlines()
        wholeFile = file.read()
        for key in keys:
            if (key not in wholeFile):
                print(key,end="")
                value = dictionary[key]
                line = "{} | {} \n".format(key, value)
                data.append(line)
        file.writelines(data)
        file.close()

def translatedDictToCsv(dictionary):
    with open(FILE_OUT_CSV, 'w+', newline='', encoding="utf-8") as csvFile:
        reader = csv.DictReader(csvFile)
        fields = ["Original","Translated"]
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        
        readerDict = dict(reader)
        fileKeys = readerDict.keys()
        inputKeys = dictionary.keys()

        writer.writeheader()
        for key in inputKeys:
            if key not in fileKeys:
                print(key,end="")
                value = dictionary[key]
                writer.writerow({"Original":key, "Translated":value})
        csvFile.close()
            
def main():
    client = translate.Client()
    characters ='''
    這來國個箇說們為時會著過對沒還祇無開見經頭從動兩長樣現將與進實點種聲話兒問機給業間甚電門東聽氣關內卻
    軍產萬體別彆處總纔場師書員華報馬張難數車應計親務記邊風戰許覺題統請愛讓認論佰義術結連遠資隊帶條變聯權
    該領傳紅決達辦運強彊區轉眾輕語滿寫識極黃臉錢黨設雙仟廣議際則單據導網專耑誰讀飛觀爭組視濟離雖編寶談隨
    劍講殺調團終樂級舉證証費爾熱響稱興約陽驚嗎漢號絕選參亞傷類備歡勢斷陳農唸腦規媽剛顯陸確澤緊幫線願楊節
    裝歲嚴鐵聞紀腳蘇標飯醫況軟擊僅續獨羅買戶護責項衛圖亂劉爺龍錯創樹靈職鄉細訴態筆塊質灣韋圍靜園輯夠賽較
    樓孫詩敵試謝懷顧驗營養麗屬惡維漸勝異負銀陣層織藥館習簡歸換絲勞婦評絡環禮壓獎趕蘭錄畫頓藝億繼優險階擔
    訪討臨吳搖練構廠協揮齊溫紙頂尋寧賣順夢劇堅雜貴舊積縣罷揚脫彈鄧鮮畢歐島載敗槍適虛預紛銷魚盤訊趙燈狀訂
    鎮罵輸詞淚財審牆聖躍執曉橋輩閃隱勁鬧監廳庫慶綠額誤納遺魯貨緩偉莊燒搶戲謂課郵榮擁獻嘆陰橫簽輪訓圓釋諸
    奪測蓋閱購縱掛擇譽檢宮儀擺奧滅慮寬紹補贊穩厲屆跡雞憶誠減針競倫鋼諾殘災喬糧譯謀礎損輛凈蕩奮膽棄煩猶稅
    鋒遙慣憑幣啟碼窮頗傾韓貿飄側賞純閉涼掃貼滾緣貝潤擴欄嚇倆藍閑鏡騎顏貧駐傑撲壯薩憂獄鳳觸戀豈俠遲輝縮蕭
    辭齡徑賴憤詢慘麥騰烏崗鋪擋帳豬勸築擠潔鄭鳴顆喪爛騙頁屍療塵飲賓緒賊廢詳湯徹轟憐鳥毀聰辯餓楓掙彎蔣違虧
    丟繞暫遞潛鴻績塗悶勵艦牽肅夾瘋惱顫艱蒼蓮鑽峽遼凱貓濤鍋罰濃鍵脈鎖鄰駕禍覽銅檔拋驅窩褲闊瑪頻禪萊嘗盜籌
    淺厭壽錦鑒趨貫撥遜賠遷襲駛懼紐蹤叢銳濕睜溝貢渾贏馳恆賢飾償纏攝擬闖賀縫飽撫冊煉憲廟誼儲馮喚貪臥擾脅譜
    閣鵬盧礙綜暈攔霧恥攤誕懸湊籠顛攜擲糾穌噸蟲繩廚漲皺賭饒礦暢噴鏢撐爐偽諒釣腸剝賺燭廈邁齒謹彌誇債剎膚癥
    欽綿誘晉悅艷貸頸踐賈轎嬌瀟賜墳頌磚鶴漁啞餅犧灘釘錫贈鈴頑鷹軌喲碩帥懶獸獵鹽飢邏驕販繪蠻敘斬呂譚凍駱潑
    謙廁嶺鮑禿倉綁薦鴨診紋龐騷嘩畝謊籃擱廂瞞腫僑疊嘯脹賦懇嬰斃謎瓊嗚竄頒頰囑駁滬賤鉤豎懲繡訝綱濱艙娛鴉獅
    凜龜窯纖寵鏈壩狹銘淵襯緬摟縛燦輿韻竊偵陝聳醬壺癢殼貞蘆輔賬撿糞濫潰隸曠繳穎妝蠟劑驟廬蘋曬攏朧膠諷揀樁
    謠墜滯誦岡紗銜膩撈攪傘鑄軀燙漿釀鵝茲搗棟纜爍詐紡錘兌辮墮覓諧綢澆淪縷蘿蔭譏蔥鞏齋幟鉛賄絨侶鍛譴洶諱鑼
    勻綽絞軸壘蘊傭晝蝕蝦謬紳鑲聾壟彥翹闡訟樞嶄瀉儉
    '''
    strList = strToSingleCharacterList(characters)
    details = client, strList
    translatedDict = translateFromList(details)
    saveToFile(translatedDict)
    print()
    translatedDictToCsv(translatedDict)
main()