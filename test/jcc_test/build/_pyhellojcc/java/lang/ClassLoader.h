#ifndef java_lang_ClassLoader_H
#define java_lang_ClassLoader_H

#include "java/lang/Object.h"

namespace java {
  namespace lang {
    class Class;
    class ClassNotFoundException;
    class String;
  }
  namespace util {
    class Enumeration;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class ClassLoader : public ::java::lang::Object {
    public:
      enum {
        mid_clearAssertionStatus_3b7a1d3d26162b85,
        mid_getParent_c3b4e13d45aa948d,
        mid_getSystemClassLoader_c3b4e13d45aa948d,
        mid_loadClass_3db5ad13abace10f,
        mid_setClassAssertionStatus_b5c0f2463d1354e7,
        mid_setDefaultAssertionStatus_4e7a2bdefbe801b3,
        mid_setPackageAssertionStatus_b5c0f2463d1354e7,
        mid_loadClass_a25db3df2ed5cbd5,
        mid_getPackage_f8e67dcd7ece1694,
        mid_setSigners_6d68747532a255d3,
        mid_getClassLoadingLock_ff07a348f6d890ba,
        mid_findClass_3db5ad13abace10f,
        mid_defineClass_41ca5a2a8a3676c0,
        mid_defineClass_a54b9bae0a183ab1,
        mid_defineClass_1c64ef94eeed56c4,
        mid_defineClass_af0f6e0f6dd5cd15,
        mid_resolveClass_24b7cc29b8390607,
        mid_findSystemClass_3db5ad13abace10f,
        mid_findLoadedClass_3db5ad13abace10f,
        mid_findResource_6fa68873b72e5dd6,
        mid_findResources_4bc0575416646ead,
        mid_registerAsParallelCapable_318f7cae9d6a33e6,
        mid_definePackage_8c1e479ffd51772e,
        mid_getPackages_e9607c4a35e971a3,
        mid_findLibrary_c79c18cd95453b7f,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit ClassLoader(jobject obj) : ::java::lang::Object(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      ClassLoader(const ClassLoader& obj) : ::java::lang::Object(obj) {}

      void clearAssertionStatus() const;
      ClassLoader getParent() const;
      static ClassLoader getSystemClassLoader();
      ::java::lang::Class loadClass(const ::java::lang::String &) const;
      void setClassAssertionStatus(const ::java::lang::String &, jboolean) const;
      void setDefaultAssertionStatus(jboolean) const;
      void setPackageAssertionStatus(const ::java::lang::String &, jboolean) const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(ClassLoader);

    class t_ClassLoader {
    public:
      PyObject_HEAD
      ClassLoader object;
      static PyObject *wrap_Object(const ClassLoader&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
