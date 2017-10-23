#ifndef java_lang_Package_H
#define java_lang_Package_H

#include "java/lang/Object.h"

namespace java {
  namespace lang {
    class NumberFormatException;
    class String;
    class Class;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class Package : public ::java::lang::Object {
    public:
      enum {
        mid_getImplementationTitle_c041e21e63165d2d,
        mid_getImplementationVendor_c041e21e63165d2d,
        mid_getImplementationVersion_c041e21e63165d2d,
        mid_getName_c041e21e63165d2d,
        mid_getPackage_f8e67dcd7ece1694,
        mid_getPackages_e9607c4a35e971a3,
        mid_getSpecificationTitle_c041e21e63165d2d,
        mid_getSpecificationVendor_c041e21e63165d2d,
        mid_getSpecificationVersion_c041e21e63165d2d,
        mid_hashCode_60df5a771df5b62d,
        mid_isCompatibleWith_1dfa664233a47103,
        mid_isSealed_318f7cae9d6a33e6,
        mid_toString_c041e21e63165d2d,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Package(jobject obj) : ::java::lang::Object(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Package(const Package& obj) : ::java::lang::Object(obj) {}

      ::java::lang::String getImplementationTitle() const;
      ::java::lang::String getImplementationVendor() const;
      ::java::lang::String getImplementationVersion() const;
      ::java::lang::String getName() const;
      static Package getPackage(const ::java::lang::String &);
      static JArray< Package > getPackages();
      ::java::lang::String getSpecificationTitle() const;
      ::java::lang::String getSpecificationVendor() const;
      ::java::lang::String getSpecificationVersion() const;
      jint hashCode() const;
      jboolean isCompatibleWith(const ::java::lang::String &) const;
      jboolean isSealed() const;
      ::java::lang::String toString() const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Package);

    class t_Package {
    public:
      PyObject_HEAD
      Package object;
      static PyObject *wrap_Object(const Package&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
