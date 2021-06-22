# shopee_code_league_2021

競賽網頁：https://careers.shopee.sg/codeleague/
競賽總共分成三個項目

## competition 1：Data Analytics
kaggle：https://www.kaggle.com/c/scl-2021-da<br/>
主辦方提供了50萬筆的訂單資料，每筆訂單包含了顧客的mail、地址以及電話<br/>
在擁有相同mail、地址或電話就被視為同一個顧客的假設下<br/>
找出哪些訂單是來自同一個顧客

## competition 2：Data Science
kaggle：https://www.kaggle.com/c/scl-2021-ds<br/>
從印尼的地址中，辨識出街道名稱(street name)以及興趣點(point of intetest;POI)<br/>
POI可以把它理解成一些會在地圖上特別被標記的地點，例如市政府、台北101等<br/>
需要特別注意的是，地址中street name跟POI都有可能是縮寫<br/>
在輸出結果是，需要把縮寫還原成它原本的名稱<br/>
<br/>
因此，這次的競賽重點可以分成兩個部分<br/>
模型訓練以及資料探索<br/>
模型訓練的主要目標就是從地址中，利用語句結構找出未知的street name及POI<br/>
<br/>
而資料探索的目的<br/>
則是從trainind data中<br/>
找出縮寫還原的規則<br/>
進一步對模型結果進行post proecess<br/>
<br/>
根據kaggle上的分數變動<br/>
在沒有post process的狀況下<br/>
大部分的組別直接將model結果上傳，分數大都落在0.6上下<br/>
因此，後期比拼的就是各組如何透過資料探索找出更多的縮寫還原的規則

## competition 3：Engineering
leadcode題大比拼<br/>
利用電商物流的題目包裝各種演算法的題目<br/>
還蠻有趣的<br/>
可惜我們組在這一階段並沒有表現得很好
