import streamlit as st
from utils import script_generator

st.title("✍️ 短视频脚本生成器")

subject = st.text_input("💡这支视频关于什么主题？")
video_length = st.number_input("⏱️视频的大致时长是多少分钟？", min_value=0.1, step=0.1)
creativity = st.slider("✨希望视频脚本的创造力是？（数字小说明更保守，数字大会有更多惊喜）", min_value=0.0,
                       max_value=1.5, value=0.2, step=0.1)
submit = st.button("生成脚本")

if submit and not subject:
    st.info("请输入视频的主题哦")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("视频长度需要大于或等于0.1分钟哦")
    st.stop()
if submit:
    with st.spinner("AI正在创作中，请稍等..."):
        search_result, title, script = script_generator(subject, video_length, creativity)
    st.success("视频脚本已生成！")
    st.subheader("🔥标题：")
    st.write(title)
    st.subheader("📝脚本内容：")
    st.write(script)
    with st.expander("维基百科搜索结果👀"):
        st.info(search_result)