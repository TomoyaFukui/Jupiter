#ifndef java_lang_Class_H
#define java_lang_Class_H

#include "java/lang/Object.h"

namespace java {
  namespace lang {
    class Package;
    class ClassNotFoundException;
    class ClassLoader;
    class InstantiationException;
    class SecurityException;
    class IllegalAccessException;
    class String;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class Class : public ::java::lang::Object {
    public:
      enum {
        mid_asSubclass_4774fc9aadd29538,
        mid_cast_5cfb9aa5c138c100,
        mid_desiredAssertionStatus_318f7cae9d6a33e6,
        mid_forName_3db5ad13abace10f,
        mid_forName_901884e88fd031f0,
        mid_getCanonicalName_c041e21e63165d2d,
        mid_getClassLoader_c3b4e13d45aa948d,
        mid_getClasses_8b92e6f57abcba7e,
        mid_getComponentType_0922d10264375499,
        mid_getDeclaredClasses_8b92e6f57abcba7e,
        mid_getDeclaringClass_0922d10264375499,
        mid_getEnclosingClass_0922d10264375499,
        mid_getEnumConstants_2fc1d90a855043f7,
        mid_getInterfaces_8b92e6f57abcba7e,
        mid_getModifiers_60df5a771df5b62d,
        mid_getName_c041e21e63165d2d,
        mid_getPackage_39e15168226e8bf5,
        mid_getSigners_2fc1d90a855043f7,
        mid_getSimpleName_c041e21e63165d2d,
        mid_getSuperclass_0922d10264375499,
        mid_getTypeName_c041e21e63165d2d,
        mid_isAnnotation_318f7cae9d6a33e6,
        mid_isAnonymousClass_318f7cae9d6a33e6,
        mid_isArray_318f7cae9d6a33e6,
        mid_isAssignableFrom_996c25acd1f494c9,
        mid_isEnum_318f7cae9d6a33e6,
        mid_isInstance_04e1a7382c29bc4b,
        mid_isInterface_318f7cae9d6a33e6,
        mid_isLocalClass_318f7cae9d6a33e6,
        mid_isMemberClass_318f7cae9d6a33e6,
        mid_isPrimitive_318f7cae9d6a33e6,
        mid_isSynthetic_318f7cae9d6a33e6,
        mid_newInstance_6a490f1da80a3003,
        mid_toGenericString_c041e21e63165d2d,
        mid_toString_c041e21e63165d2d,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Class(jobject obj) : ::java::lang::Object(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Class(const Class& obj) : ::java::lang::Object(obj) {}

      Class asSubclass(const Class &) const;
      ::java::lang::Object cast(const ::java::lang::Object &) const;
      jboolean desiredAssertionStatus() const;
      static Class forName(const ::java::lang::String &);
      static Class forName(const ::java::lang::String &, jboolean, const ::java::lang::ClassLoader &);
      ::java::lang::String getCanonicalName() const;
      ::java::lang::ClassLoader getClassLoader() const;
      JArray< Class > getClasses() const;
      Class getComponentType() const;
      JArray< Class > getDeclaredClasses() const;
      Class getDeclaringClass() const;
      Class getEnclosingClass() const;
      JArray< ::java::lang::Object > getEnumConstants() const;
      JArray< Class > getInterfaces() const;
      jint getModifiers() const;
      ::java::lang::String getName() const;
      ::java::lang::Package getPackage() const;
      JArray< ::java::lang::Object > getSigners() const;
      ::java::lang::String getSimpleName() const;
      Class getSuperclass() const;
      ::java::lang::String getTypeName() const;
      jboolean isAnnotation() const;
      jboolean isAnonymousClass() const;
      jboolean isArray() const;
      jboolean isAssignableFrom(const Class &) const;
      jboolean isEnum() const;
      jboolean isInstance(const ::java::lang::Object &) const;
      jboolean isInterface() const;
      jboolean isLocalClass() const;
      jboolean isMemberClass() const;
      jboolean isPrimitive() const;
      jboolean isSynthetic() const;
      ::java::lang::Object newInstance() const;
      ::java::lang::String toGenericString() const;
      ::java::lang::String toString() const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Class);

    class t_Class {
    public:
      PyObject_HEAD
      Class object;
      PyTypeObject *parameters[1];
      static PyTypeObject **parameters_(t_Class *self)
      {
        return (PyTypeObject **) &(self->parameters);
      }
      static PyObject *wrap_Object(const Class&);
      static PyObject *wrap_jobject(const jobject&);
      static PyObject *wrap_Object(const Class&, PyTypeObject *);
      static PyObject *wrap_jobject(const jobject&, PyTypeObject *);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
