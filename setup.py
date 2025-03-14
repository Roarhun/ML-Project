from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .' #เรียกใช้ไฟล์ setup อัตโนมัติ แต่ต้องตัดออกจาก list requirements เพราะไม่ใช่ library ที่ต้อง install
def get_requirements(file_path:str)->List[str]:
    '''Returns list of requirements'''
    requirements=[]
    with open(file_path) as file_object:
        requirements=file_object.readlines() #อ่านบรรทัดในไฟล์ requirements 
        requirements=[req.replace('\n','') for req in requirements] #แทนที่ \n ด้วยที่ว่าง เพราะตอนขึ้นบรรทัดใหม่จะมีติดมา ทำให้อ่านชื่อผิด

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name="ML_Project",
    version="0.0.1",
    author="Roarhun",
    author_email="benjawan.manda731@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)