#ifndef java_io_PrintWriter_H
#define java_io_PrintWriter_H

#include "java/io/Writer.h"

namespace java {
  namespace lang {
    class Class;
    class Object;
    class CharSequence;
    class String;
  }
}
template<class T> class JArray;

namespace java {
  namespace io {

    class PrintWriter : public ::java::io::Writer {
    public:
      enum {
        mid_init$_38d57a80b9fe8948,
        mid_init$_6c1ced5c118affbd,
        mid_init$_f6990a6542b56458,
        mid_init$_0be462401b6d11a7,
        mid_append_14679c9085946363,
        mid_append_b333bb0e2ebd6eeb,
        mid_append_068eb4d597879c27,
        mid_checkError_318f7cae9d6a33e6,
        mid_close_3b7a1d3d26162b85,
        mid_flush_3b7a1d3d26162b85,
        mid_format_7ad82831eb68e788,
        mid_print_00f6aa63d2ba4dac,
        mid_print_625495ddbdca45a4,
        mid_print_a9395152fa63d3b0,
        mid_print_1e3a1ae808486483,
        mid_print_4e7a2bdefbe801b3,
        mid_print_eb5fd921f75df46a,
        mid_print_38d57a80b9fe8948,
        mid_print_ee30b01cc5d9d615,
        mid_print_4454b3633e331cef,
        mid_printf_7ad82831eb68e788,
        mid_println_3b7a1d3d26162b85,
        mid_println_4454b3633e331cef,
        mid_println_ee30b01cc5d9d615,
        mid_println_00f6aa63d2ba4dac,
        mid_println_38d57a80b9fe8948,
        mid_println_eb5fd921f75df46a,
        mid_println_a9395152fa63d3b0,
        mid_println_1e3a1ae808486483,
        mid_println_4e7a2bdefbe801b3,
        mid_println_625495ddbdca45a4,
        mid_write_ee30b01cc5d9d615,
        mid_write_a9395152fa63d3b0,
        mid_write_38d57a80b9fe8948,
        mid_write_7b7b455231dae263,
        mid_write_328bb6dd18104856,
        mid_setError_3b7a1d3d26162b85,
        mid_clearError_3b7a1d3d26162b85,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit PrintWriter(jobject obj) : ::java::io::Writer(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      PrintWriter(const PrintWriter& obj) : ::java::io::Writer(obj) {}

      PrintWriter(const ::java::lang::String &);
      PrintWriter(const ::java::io::Writer &);
      PrintWriter(const ::java::lang::String &, const ::java::lang::String &);
      PrintWriter(const ::java::io::Writer &, jboolean);

      PrintWriter append(const ::java::lang::CharSequence &) const;
      PrintWriter append(jchar) const;
      PrintWriter append(const ::java::lang::CharSequence &, jint, jint) const;
      jboolean checkError() const;
      void close() const;
      void flush() const;
      PrintWriter format(const ::java::lang::String &, const JArray< ::java::lang::Object > &) const;
      void print(jfloat) const;
      void print(jlong) const;
      void print(jint) const;
      void print(jchar) const;
      void print(jboolean) const;
      void print(const ::java::lang::Object &) const;
      void print(const ::java::lang::String &) const;
      void print(const JArray< jchar > &) const;
      void print(jdouble) const;
      PrintWriter printf(const ::java::lang::String &, const JArray< ::java::lang::Object > &) const;
      void println() const;
      void println(jdouble) const;
      void println(const JArray< jchar > &) const;
      void println(jfloat) const;
      void println(const ::java::lang::String &) const;
      void println(const ::java::lang::Object &) const;
      void println(jint) const;
      void println(jchar) const;
      void println(jboolean) const;
      void println(jlong) const;
      void write(const JArray< jchar > &) const;
      void write(jint) const;
      void write(const ::java::lang::String &) const;
      void write(const JArray< jchar > &, jint, jint) const;
      void write(const ::java::lang::String &, jint, jint) const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace io {
    extern PyTypeObject PY_TYPE(PrintWriter);

    class t_PrintWriter {
    public:
      PyObject_HEAD
      PrintWriter object;
      static PyObject *wrap_Object(const PrintWriter&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
