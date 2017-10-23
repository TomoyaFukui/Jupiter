#ifndef jcc_test_HelloJCC_H
#define jcc_test_HelloJCC_H

#include "java/lang/Object.h"

namespace java {
  namespace lang {
    class Integer;
    class String;
    class Class;
  }
}
template<class T> class JArray;

namespace jcc_test {

  class HelloJCC : public ::java::lang::Object {
  public:
    enum {
      mid_init$_38d57a80b9fe8948,
      mid_init$_62ca3504c6e80f45,
      mid_main_93dc42246c5a16dc,
      max_mid
    };

    static ::java::lang::Class *class$;
    static jmethodID *mids$;
    static bool live$;
    static jclass initializeClass(bool);

    explicit HelloJCC(jobject obj) : ::java::lang::Object(obj) {
      if (obj != NULL)
        env->getClass(initializeClass);
    }
    HelloJCC(const HelloJCC& obj) : ::java::lang::Object(obj) {}

    HelloJCC(const ::java::lang::String &);
    HelloJCC(const ::java::lang::Integer &);

    static void main(const JArray< ::java::lang::String > &);
  };
}

#include <Python.h>

namespace jcc_test {
  extern PyTypeObject PY_TYPE(HelloJCC);

  class t_HelloJCC {
  public:
    PyObject_HEAD
    HelloJCC object;
    static PyObject *wrap_Object(const HelloJCC&);
    static PyObject *wrap_jobject(const jobject&);
    static void install(PyObject *module);
    static void initialize(PyObject *module);
  };
}

#endif
