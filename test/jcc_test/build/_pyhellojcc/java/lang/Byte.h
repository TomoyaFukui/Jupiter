#ifndef java_lang_Byte_H
#define java_lang_Byte_H

#include "java/lang/Number.h"

namespace java {
  namespace lang {
    class Class;
    class Comparable;
    class Object;
    class NumberFormatException;
    class String;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class Byte : public ::java::lang::Number {
    public:
      enum {
        mid_init$_4ae782e2002f2005,
        mid_init$_38d57a80b9fe8948,
        mid_byteValue_51018f1683a6b595,
        mid_compare_dd3bab549f1269ef,
        mid_compareTo_580c045618437d83,
        mid_decode_52f1cac43c85245c,
        mid_doubleValue_746fdfc2336a8dce,
        mid_equals_04e1a7382c29bc4b,
        mid_floatValue_4e51965d8682d4e7,
        mid_hashCode_60df5a771df5b62d,
        mid_hashCode_d509c008f6ebc11d,
        mid_intValue_60df5a771df5b62d,
        mid_longValue_0a482dcd1f56375a,
        mid_parseByte_33060f793072446b,
        mid_parseByte_fd1a035ce7af79d1,
        mid_shortValue_3e271dc4ae1ecc4b,
        mid_toString_c041e21e63165d2d,
        mid_toString_3e2d3cc2f2361bf0,
        mid_toUnsignedInt_d509c008f6ebc11d,
        mid_toUnsignedLong_78c495804247ba9f,
        mid_valueOf_c1bf298dc5c7510b,
        mid_valueOf_52f1cac43c85245c,
        mid_valueOf_94243246b4507eee,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Byte(jobject obj) : ::java::lang::Number(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Byte(const Byte& obj) : ::java::lang::Number(obj) {}

      static jint BYTES;
      static jbyte MAX_VALUE;
      static jbyte MIN_VALUE;
      static jint SIZE;
      static ::java::lang::Class *TYPE;

      Byte(jbyte);
      Byte(const ::java::lang::String &);

      jbyte byteValue() const;
      static jint compare(jbyte, jbyte);
      jint compareTo(const Byte &) const;
      static Byte decode(const ::java::lang::String &);
      jdouble doubleValue() const;
      jboolean equals(const ::java::lang::Object &) const;
      jfloat floatValue() const;
      jint hashCode() const;
      static jint hashCode(jbyte);
      jint intValue() const;
      jlong longValue() const;
      static jbyte parseByte(const ::java::lang::String &);
      static jbyte parseByte(const ::java::lang::String &, jint);
      jshort shortValue() const;
      ::java::lang::String toString() const;
      static ::java::lang::String toString(jbyte);
      static jint toUnsignedInt(jbyte);
      static jlong toUnsignedLong(jbyte);
      static Byte valueOf(jbyte);
      static Byte valueOf(const ::java::lang::String &);
      static Byte valueOf(const ::java::lang::String &, jint);
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Byte);

    class t_Byte {
    public:
      PyObject_HEAD
      Byte object;
      static PyObject *wrap_Object(const Byte&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
