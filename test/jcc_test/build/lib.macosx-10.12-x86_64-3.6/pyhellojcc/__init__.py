
import os
from . import _pyhellojcc

__dir__ = os.path.abspath(os.path.dirname(__file__))

class JavaError(Exception):
  def getJavaException(self):
    return self.args[0]
  def __str__(self):
    writer = StringWriter()
    self.getJavaException().printStackTrace(PrintWriter(writer))
    return u"\n".join((unicode(super(JavaError, self)), u"    Java stacktrace:", unicode(writer)))

class InvalidArgsError(Exception):
  pass

_pyhellojcc._set_exception_types(JavaError, InvalidArgsError)
CLASSPATH = [os.path.join(__dir__, "HelloJCC.jar")]
CLASSPATH = os.pathsep.join(CLASSPATH)
_pyhellojcc.CLASSPATH = CLASSPATH
_pyhellojcc._set_function_self(_pyhellojcc.initVM, _pyhellojcc)

from ._pyhellojcc import *
