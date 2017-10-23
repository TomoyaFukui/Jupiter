#ifndef java_lang_String_H
#define java_lang_String_H

#include "java/lang/Object.h"

namespace java {
  namespace lang {
    class Iterable;
    class Class;
    class StringBuffer;
    class Comparable;
    class StringBuilder;
    class CharSequence;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class String : public ::java::lang::Object {
    public:
      enum {
        mid_init$_3b7a1d3d26162b85,
        mid_init$_e3f6d981bb98002b,
        mid_init$_e9f9ecbb9bb29bce,
        mid_init$_0aa635e49c766730,
        mid_init$_ee30b01cc5d9d615,
        mid_init$_8cbfd868bfdff135,
        mid_init$_a4aa77e2acc83203,
        mid_init$_881b8ae3c0bdb376,
        mid_init$_984e72d4375fd50f,
        mid_init$_7b7b455231dae263,
        mid_init$_1e123a7bfc92a801,
        mid_init$_42f870ff4481584e,
        mid_charAt_bdde8923c8d84ea7,
        mid_codePointAt_4b23a339ec27bbb3,
        mid_codePointBefore_4b23a339ec27bbb3,
        mid_codePointCount_3d7ede988f6b3a33,
        mid_compareTo_9a1fdcf5cfdf78dc,
        mid_compareToIgnoreCase_9a1fdcf5cfdf78dc,
        mid_concat_c79c18cd95453b7f,
        mid_contains_a093ae255199407d,
        mid_contentEquals_9bacd0c2c4bd71ea,
        mid_contentEquals_a093ae255199407d,
        mid_copyValueOf_ad859f3cfef72b92,
        mid_copyValueOf_cc12409b36f61dbe,
        mid_endsWith_1dfa664233a47103,
        mid_equals_04e1a7382c29bc4b,
        mid_equalsIgnoreCase_1dfa664233a47103,
        mid_format_e98520bddae6a520,
        mid_getBytes_b06da5bfeb7ad4b6,
        mid_getBytes_625b99a7c088ddaf,
        mid_getBytes_8b283c8087c7fed3,
        mid_getChars_b97bea56ebef93e7,
        mid_hashCode_60df5a771df5b62d,
        mid_indexOf_4b23a339ec27bbb3,
        mid_indexOf_9a1fdcf5cfdf78dc,
        mid_indexOf_e65105c140eb7151,
        mid_indexOf_3d7ede988f6b3a33,
        mid_intern_c041e21e63165d2d,
        mid_isEmpty_318f7cae9d6a33e6,
        mid_join_dd88d98cf93c3794,
        mid_join_55db8d22d92036d6,
        mid_lastIndexOf_4b23a339ec27bbb3,
        mid_lastIndexOf_9a1fdcf5cfdf78dc,
        mid_lastIndexOf_3d7ede988f6b3a33,
        mid_lastIndexOf_e65105c140eb7151,
        mid_length_60df5a771df5b62d,
        mid_matches_1dfa664233a47103,
        mid_offsetByCodePoints_3d7ede988f6b3a33,
        mid_regionMatches_b3496c6a4004b75a,
        mid_regionMatches_bb9b26b6d1e5dc56,
        mid_replace_d059205c579400c9,
        mid_replace_3d105a3ff9bb821d,
        mid_replaceAll_4d5d4b421f989dfc,
        mid_replaceFirst_4d5d4b421f989dfc,
        mid_split_9d1093a8564b26d8,
        mid_split_8f69e25c6c689b02,
        mid_startsWith_1dfa664233a47103,
        mid_startsWith_5f2909f6abb49638,
        mid_subSequence_4648df63ce82f704,
        mid_substring_ab09aaf2e63107e3,
        mid_substring_5b238f74b18cd9ba,
        mid_toCharArray_c6f65d298757269e,
        mid_toLowerCase_c041e21e63165d2d,
        mid_toString_c041e21e63165d2d,
        mid_toUpperCase_c041e21e63165d2d,
        mid_trim_c041e21e63165d2d,
        mid_valueOf_82ceb9edccd24fa3,
        mid_valueOf_6b4670e37be63f0c,
        mid_valueOf_ea6d2a082bd69826,
        mid_valueOf_ad859f3cfef72b92,
        mid_valueOf_7d2d6127fa523a6f,
        mid_valueOf_3ef4f0a5c27c2560,
        mid_valueOf_6cc2f594436f7b3d,
        mid_valueOf_ab09aaf2e63107e3,
        mid_valueOf_cc12409b36f61dbe,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit String(jobject obj) : ::java::lang::Object(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      String(const String& obj) : ::java::lang::Object(obj) {}

      String();
      String(const ::java::lang::StringBuilder &);
      String(const ::java::lang::StringBuffer &);
      String(const JArray< jbyte > &);
      String(const JArray< jchar > &);
      String(const JArray< jbyte > &, const String &);
      String(const JArray< jbyte > &, jint);
      String(const JArray< jbyte > &, jint, jint);
      String(const JArray< jint > &, jint, jint);
      String(const JArray< jchar > &, jint, jint);
      String(const JArray< jbyte > &, jint, jint, const String &);
      String(const JArray< jbyte > &, jint, jint, jint);

      jchar charAt(jint) const;
      jint codePointAt(jint) const;
      jint codePointBefore(jint) const;
      jint codePointCount(jint, jint) const;
      jint compareTo(const String &) const;
      jint compareToIgnoreCase(const String &) const;
      String concat(const String &) const;
      jboolean contains(const ::java::lang::CharSequence &) const;
      jboolean contentEquals(const ::java::lang::StringBuffer &) const;
      jboolean contentEquals(const ::java::lang::CharSequence &) const;
      static String copyValueOf(const JArray< jchar > &);
      static String copyValueOf(const JArray< jchar > &, jint, jint);
      jboolean endsWith(const String &) const;
      jboolean equals(const ::java::lang::Object &) const;
      jboolean equalsIgnoreCase(const String &) const;
      static String format(const String &, const JArray< ::java::lang::Object > &);
      JArray< jbyte > getBytes() const;
      JArray< jbyte > getBytes(const String &) const;
      void getBytes(jint, jint, const JArray< jbyte > &, jint) const;
      void getChars(jint, jint, const JArray< jchar > &, jint) const;
      jint hashCode() const;
      jint indexOf(jint) const;
      jint indexOf(const String &) const;
      jint indexOf(const String &, jint) const;
      jint indexOf(jint, jint) const;
      String intern() const;
      jboolean isEmpty() const;
      static String join(const ::java::lang::CharSequence &, const JArray< ::java::lang::CharSequence > &);
      static String join(const ::java::lang::CharSequence &, const ::java::lang::Iterable &);
      jint lastIndexOf(jint) const;
      jint lastIndexOf(const String &) const;
      jint lastIndexOf(jint, jint) const;
      jint lastIndexOf(const String &, jint) const;
      jint length() const;
      jboolean matches(const String &) const;
      jint offsetByCodePoints(jint, jint) const;
      jboolean regionMatches(jint, const String &, jint, jint) const;
      jboolean regionMatches(jboolean, jint, const String &, jint, jint) const;
      String replace(jchar, jchar) const;
      String replace(const ::java::lang::CharSequence &, const ::java::lang::CharSequence &) const;
      String replaceAll(const String &, const String &) const;
      String replaceFirst(const String &, const String &) const;
      JArray< String > split(const String &) const;
      JArray< String > split(const String &, jint) const;
      jboolean startsWith(const String &) const;
      jboolean startsWith(const String &, jint) const;
      ::java::lang::CharSequence subSequence(jint, jint) const;
      String substring(jint) const;
      String substring(jint, jint) const;
      JArray< jchar > toCharArray() const;
      String toLowerCase() const;
      String toString() const;
      String toUpperCase() const;
      String trim() const;
      static String valueOf(jchar);
      static String valueOf(const ::java::lang::Object &);
      static String valueOf(jboolean);
      static String valueOf(const JArray< jchar > &);
      static String valueOf(jdouble);
      static String valueOf(jfloat);
      static String valueOf(jlong);
      static String valueOf(jint);
      static String valueOf(const JArray< jchar > &, jint, jint);
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(String);

    class t_String {
    public:
      PyObject_HEAD
      String object;
      static PyObject *wrap_Object(const String&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
