from PIL import Image
import PackFilePath
path_file = input('请输入文件位置：')
path_file = PackFilePath.PFP_Backslashes_Slashes(path_file)
to = input('请输入文件保存文件位置：')
to_ho = input('请输入转换文件后缀：')
to = PackFilePath.PFP_Backslashes_Slashes(to)

im = Image.open(path_file)  # 此时返回一个新的image对象，转换图片模式
if to_ho == 'jpg':
    im = im.convert('RGB')
a = f'{to}.{to_ho}'
im.save(a)