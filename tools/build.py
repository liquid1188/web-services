import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pages1
out = [pages1.home(), pages1.work(), pages1.gallery()]
for mod in ("pages2", "pages3"):
    try:
        m = __import__(mod); out += m.build()
    except ModuleNotFoundError:
        pass
print("wrote", len(out), "pages:", ", ".join(out))
