s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
    ord('\t'):' ',
    ord('\f'):' ',
    ord('\r'):None,
}
a = s.translate(remap)
print(a)

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
b1 = b.translate(cmb_chrs)
print(b1)

