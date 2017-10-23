#ifndef java_lang_StringBuilder_H
#define java_lang_StringBuilder_H

#include "java/lang/AbstractStringBuilder.h"

namespace java {
  namespace lang {
    class Class;
    class StringBuffer;
    class Object;
    class CharSequence;
    class String;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class StringBuilder : public ::java::lang::AbstractStringBuilder {
    public:
      enum {
        mid_init$_3b7a1d3d26162b85,
        mid_init$_ff3cc5064b2f599b,
        mid_init$_38d57a80b9fe8948,
        mid_init$_a9395152fa63d3b0,
        mid_append_af7d2abbcfd14857,
        mid_append_615db9cc8130353e,
        mid_append_5b23a8244b9a7150,
        mid_append_ebe660f89dd63af9,
        mid_append_2c67186a89fb716a,
        mid_append_50bc4c45d6d1ccb0,
        mid_append_7c57ac4532fb10c6,
        mid_append_b1969b95267bc710,
        mid_append_abe9c630a6bcec9a,
        mid_append_75d8ec5fd89b4c81,
        mid_append_9808c39286a58fb4,
        mid_append_86a23dc66ce8be4e,
        mid_append_1be669dbfa8a5f42,
        mid_appendCodePoint_ebe660f89dd63af9,
        mid_delete_ad6c2ebf815e7874,
        mid_deleteCharAt_ebe660f89dd63af9,
        mid_indexOf_9a1fdcf5cfdf78dc,
        mid_indexOf_e65105c140eb7151,
        mid_insert_41aa9b40506a0c7c,
        mid_insert_c9d73301c404c2b1,
        mid_insert_8dbeeea672a0f6a0,
        mid_insert_ad6c2ebf815e7874,
        mid_insert_2c7cf152a89adacc,
        mid_insert_f7f2e629629f9764,
        mid_insert_fd15656206a5851f,
        mid_insert_b889c6353701bffb,
        mid_insert_c15637c39fa9b9d0,
        mid_insert_5a00b5ac4d30082a,
        mid_insert_cf2bb79cf264d07b,
        mid_insert_168eaacd337739a9,
        mid_lastIndexOf_9a1fdcf5cfdf78dc,
        mid_lastIndexOf_e65105c140eb7151,
        mid_replace_dd655b1c75d33bab,
        mid_reverse_f0c340607bb6e2bc,
        mid_toString_c041e21e63165d2d,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit StringBuilder(jobject obj) : ::java::lang::AbstractStringBuilder(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      StringBuilder(const StringBuilder& obj) : ::java::lang::AbstractStringBuilder(obj) {}

      StringBuilder();
      StringBuilder(const ::java::lang::CharSequence &);
      StringBuilder(const ::java::lang::String &);
      StringBuilder(jint);

      StringBuilder append(jboolean) const;
      StringBuilder append(const ::java::lang::CharSequence &) const;
      StringBuilder append(jchar) const;
      StringBuilder append(jint) const;
      StringBuilder append(const ::java::lang::StringBuffer &) const;
      StringBuilder append(const JArray< jchar > &) const;
      StringBuilder append(jdouble) const;
      StringBuilder append(const ::java::lang::String &) const;
      StringBuilder append(const ::java::lang::Object &) const;
      StringBuilder append(jlong) const;
      StringBuilder append(jfloat) const;
      StringBuilder append(const ::java::lang::CharSequence &, jint, jint) const;
      StringBuilder append(const JArray< jchar > &, jint, jint) const;
      StringBuilder appendCodePoint(jint) const;
      StringBuilder delete$(jint, jint) const;
      StringBuilder deleteCharAt(jint) const;
      jint indexOf(const ::java::lang::String &) const;
      jint indexOf(const ::java::lang::String &, jint) const;
      StringBuilder insert(jint, jdouble) const;
      StringBuilder insert(jint, jfloat) const;
      StringBuilder insert(jint, jlong) const;
      StringBuilder insert(jint, jint) const;
      StringBuilder insert(jint, const ::java::lang::Object &) const;
      StringBuilder insert(jint, const ::java::lang::String &) const;
      StringBuilder insert(jint, const JArray< jchar > &) const;
      StringBuilder insert(jint, const ::java::lang::CharSequence &) const;
      StringBuilder insert(jint, jboolean) const;
      StringBuilder insert(jint, jchar) const;
      StringBuilder insert(jint, const JArray< jchar > &, jint, jint) const;
      StringBuilder insert(jint, const ::java::lang::CharSequence &, jint, jint) const;
      jint lastIndexOf(const ::java::lang::String &) const;
      jint lastIndexOf(const ::java::lang::String &, jint) const;
      StringBuilder replace(jint, jint, const ::java::lang::String &) const;
      StringBuilder reverse() const;
      ::java::lang::String toString() const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(StringBuilder);

    class t_StringBuilder {
    public:
      PyObject_HEAD
      StringBuilder object;
      static PyObject *wrap_Object(const StringBuilder&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
