import requests
import m3u8

url = "https://playcdn.tvallseries.com/6m54r6pbsbf9mxq/default-m3u8/_"
url1 = "https://playcdn.tvallseries.com/6y83zfxg8tx21qx/default-m3u8/_"
url2 = 'https://playcdn.tvallseries.com/zv1shftr3z6h57t/default-m3u8/_'
url3 = "https://playcdn.tvallseries.com/avlolo2ukhh78et/default-m3u8/_"
url4 = "https://playcdn.tvallseries.com/l87n2wl8rz23y56/default-m3u8/_"
url5 = "https://playcdn.tvallseries.com/6m54r6pbsbf9mxq/default-m3u8/_"
url6 = "https://playcdn.tvallseries.com/f32qbw9bkpluo0d/default-m3u8/_"
url7 = "https://playcdn.tvallseries.com/d05s7uuvkfb9ecy/default-m3u8/_"







folderParth = r"E:\เขียนโปรแกรม\python\Project1"
# chunk_size = 265

# print(respond.status_code)
# print(respond.content)
# print(type(m3u8_master))
# print(m3u8_master.data['segments'][0]['uri'])

respond = requests.get(url5)
m3u8_master = m3u8.loads(respond.text)
MasterData = m3u8_master.data
dataVedio = MasterData['segments']
SegmentUrl = []
count = 0


with open("MrRobot_Seasons1_ep7.ts","wb") as folderParth:
    for segment in MasterData['segments']:
        url = "https:" + segment['uri']
        r = requests.get(url)
        folderParth.write(r.content)
        print("Success bit file" + str(count))
        count += 1
print("Download Success")

# print(r.content)
# while True:
#     if count < len(dataVedio):
#         # print(dataVedio[count]['uri'])
#         # print(respond.content)
#         SegmentUrl.append(dataVedio[count]['uri'])
#         r = requests.get(" https:" + MasterData['segments'][count]['uri'])
#         with open("newfile.ts","wb") as folderParth:
#             for segment in MasterData['segments']:
#                 url = "https:" + segment['uri']
#                 r = requests.get(url)
#                 folderParth.write(r.content)
#         count+=1
#     else:
#         break



# print("Success")
# print(count)
# print(MasterData.keys())
# print(len(dataVedio))
# print(respond.content)
# print(MasterData)
# print(SegmentUrl)
# print(Urlrequest)
# respond = requests.get(url, stream=True)
# with open("nwefile.ts","wb") as folderParth:
    # folderParth.write(respond)
    # for chunk in respond.iter_content(chunk_size=chunk_size):
    #     folderParth.write(chunk)
