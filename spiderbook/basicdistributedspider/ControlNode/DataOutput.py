# coding:utf-8

import codecs
import time


# 数据存储器
# 对生成的文件按照当前世界进行命名，以避免重复，同时对文件进行缓存写入。
class DataOutput(object):
    def __init__(self):
        self.filepath = 'baike_%s.html' % (time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
        self.output_head(self.filepath)
        self.datas = []

    # 解析的数据存储到内存中
    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) > 10:
            self.output_html(self.filepath)

    def output_head(self, path):
        '''
        将HTML头写进去
        :param path:
        :return:
        '''
        fout = codecs.open(path, 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        fout.close()

    # 将存储的数据输出为指定的文件格式，此处我们为HTML格式
    # def output_html(self):
    def output_html(self, path):
        '''
        将数据写入HTML文件中
        :param path:文件路径
        :return:
        '''
        fout = codecs.open(path, 'a', encoding='utf-8')
        # fout.write('<html>')
        # fout.write('<body>')
        # fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('<tr>')
            self.datas.remove(data)
        # fout.write('</table>')
        # fout.write('</body>')
        # fout.write('</html>')
        fout.close()

    def output_end(self, path):
        '''
        输出HTML结束
        :param path:文件存储路径
        :return:
        '''
        fout = codecs.open(path, 'a', encoding='utf-8')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
