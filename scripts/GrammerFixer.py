# 扫描你的文本并纠正语法错误
# pip install happytransformer
from happytransformer import HappyTextToText as HappyTTT
from happytransformer import TTSettings
def Grammer_Fixer(Text):
    Grammer = HappyTTT("T5","prithivida/grammar_error_correcter_v1")
    config = TTSettings(do_sample=True, top_k=10, max_length=100)
    corrected = Grammer.generate_text(Text, args=config)
    print("Corrected Text: ", corrected.text)
Text = "This is smple tet we how know this"
Grammer_Fixer(Text)