from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper

def script_generator(subject, video_length, creativity):
   title_template = ChatPromptTemplate.from_messages(
       [
           ("human", "请为'{subject}'这个主题创作一个吸引人的视频标题")
       ]
   )
   body_template = ChatPromptTemplate.from_messages(
       [
           ("human",
            """"你是一位年轻有活力的短视频博主，会定期在抖音、快手、TikTok上发布优质的视频内容，以轻松幽默的风格和犀利的洞察视角著称，获得全网千万粉丝。
            根据以下标题和相关信息，为你的频道写一个视频口播脚本。
            视频标题：{title}，视频时长：{duration}分钟，生成的脚本文本长度需要考虑视频时长要求，一般1分钟的口播脚本大概包含100-250个字。
            开头抓住观众眼球，快速切入主题；中间段需要占据大量篇幅，提供知识点，体现你专业的分析和洞察能力；结尾处以幽默诙谐的方式收尾，让观众记住你的风格。
            脚本格式按照【开头、中间、结尾】分隔。
            注意你的粉丝群体是18-30岁的都市独立女性，需要用吸引她们的方式进行表达。
            脚本内容可以结合以下维基百科搜索出的信息，但仅作参考，只结合相关内容即可，对不相关的进行忽略：
            '''{wikipedia_search}'''""")
       ]
   )

   model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key = "sk-OalU6JpC0YTzmYciAb336dAcB8854dCcAc777499C991Df1f",
                      openai_api_base="https://api.aigc369.com/v1", temperature=creativity)
   title_chain = title_template | model
   body_chain = body_template | model

   title = title_chain.invoke({"subject": subject}).content

   search = WikipediaAPIWrapper(language="zh")
   search_result = search.run(subject)

   body = body_chain.invoke({"title":title, "duration":video_length, "wikipedia_search":search_result}).content

   return search_result, title, body

#print(script_generator("苹果Vision Pro", 5, 0.7))