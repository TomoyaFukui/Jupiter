#ifndef java_lang_Short_H
#define java_lang_Short_H

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

    class Short : public ::java::lang::Number {
    public:
      enum {
        mid_init$_1d5e76b0d1ff996b,
        mid_init$_38d57a80b9fe8948,
        mid_byteValue_51018f1683a6b595,
        mid_compare_fd1c99d3b8e6358d,
        mid_compareTo_026e0f72b4764711,
        mid_decode_e18c8797d0875fab,
        mid_doubleValue_746fdfc2336a8dce,
        mid_equals_04e1a7382c29bc4b,
        mid_floatValue_4e51965d8682d4e7,
        mid_hashCode_60df5a771df5b62d,
        mid_hashCode_db8176b0b41c5242,
        mid_intValue_60df5a771df5b62d,
        mid_longValue_0a482dcd1f56375a,
        mid_parseShort_08e1e4518fd65a2c,
        mid_parseShort_277d20e112906cfb,
        mid_reverseBytes_66c589924122c889,
        mid_shortValue_3e271dc4ae1ecc4b,
        mid_toString_c041e21e63165d2d,
        mid_toString_16d144baec28fe9d,
        mid_toUnsignedInt_db8176b0b41c5242,
        mid_toUnsignedLong_979b1c7e23ecda06,
        mid_valueOf_82e3959169cb2447,
        mid_valueOf_e18c8797d0875fab,
        mid_valueOf_4dba6c05c2e06f44,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Short(jobject obj) : ::java::lang::Number(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Short(const Short& obj) : ::java::lang::Number(obj) {}

      static jint BYTES;
      static jshort MAX_VALUE;
      static jshort MIN_VALUE;
      static jint SIZE;
      static ::java::lang::Class *TYPE;

      Short(jshort);
      Short(const ::java::lang::String &);

      jbyte byteValue() const;
      static jint compare(jshort, jshort);
      jint compareTo(const Short &) const;
      static Short decode(const ::java::lang::String &);
      jdouble doubleValue() const;
      jboolean equals(const ::java::lang::Object &) const;
      jfloat floatValue() const;
      jint hashCode() const;
      static jint hashCode(jshort);
      jint intValue() const;
      jlong longValue() const;
      static jshort parseShort(const ::java::lang::String &);
      static jshort parseShort(const ::java::lang::String &, jint);
      static jshort reverseBytes(jshort);
      jshort shortValue() const;
      ::java::lang::String toString() const;
      static ::java::lang::String toString(jshort);
      static jint toUnsignedInt(jshort);
      static jlong toUnsignedLong(jshort);
      static Short valueOf(jshort);
      static Short valueOf(const ::java::lang::String &);
      static Short valueOf(const ::java::lang::String &, jint);
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Short);

    class t_Short {
    public:
      PyObject_HEAD
      Short object;
      static PyObject *wrap_Object(const Short&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
