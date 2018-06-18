#coding:utf8
# 清除HTMLr所有格式并且 删除换行与回车等，只显示文本
import re
def HtmlFormat_Clear(content="你需要清除HTML格式的内容"):
    dr = re.compile(r'<[^>]+>',re.S)  #将正则表达式编辑成一个对像  意思是从<开始匹配，匹配所有不是>的内容，至到出现>为止
    content = dr.sub('',content)  #把所有<>之间的所有字符全替换为空
    content=re.sub('\n','',content)   #去除换行
    content=re.sub('\s','',content)  #去除空白字符  \s是指空白，包括空格、换行、tab缩进等所有的空白  \S刚好相反
    content=re.sub('&nbsp;','',content)   #去除空格
    print content
    # return content

if __name__=="__main__":
    content="""<p style="font-family:'Microsoft YaHei', SimSun, Helvetica, sans-serif;font-size:14px;">
        <b>所属公司：</b>深圳吉祥
    </p>
    <p style="font-family:'Microsoft YaHei', SimSun, Helvetica, sans-serif;font-size:14px;">
        <b>从业经历：</b>10年
    </p>
    <p style="font-family:'Microsoft YaHei', SimSun, Helvetica, sans-serif;font-size:14px;">
        <strong>擅长风格</strong>：现代简约，欧式，新中式，现代奢华，美式 ，地中海
    </p>
    <p style="font-family:'Microsoft YaHei', SimSun, Helvetica, sans-serif;font-size:14px;">
        <strong>主要作品</strong>：公园大地 万科城别墅 星河时代&nbsp; 百合盛世洋房 保利上城
    </p>
    <p style="font-family:'Microsoft YaHei', SimSun, Helvetica, sans-serif;font-size:14px;">
        <strong>设计理念</strong>：<span>设计以人为本，，细节决定完美，设计的精髓能使设计更具有个性化和专业化。</span>
    </p>"""
    HtmlFormat_Clear(content)
