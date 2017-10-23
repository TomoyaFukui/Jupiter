#ifndef java_lang_Character_H
#define java_lang_Character_H

#include "java/lang/Object.h"

namespace java {
  namespace lang {
    class Class;
    class Comparable;
    class CharSequence;
    class String;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class Character : public ::java::lang::Object {
    public:
      enum {
        mid_init$_1e3a1ae808486483,
        mid_charCount_4b23a339ec27bbb3,
        mid_charValue_27667b9767feeda0,
        mid_codePointAt_98218a2785b3f776,
        mid_codePointAt_4c67fb52be240c28,
        mid_codePointAt_b92cf8f753e2d54d,
        mid_codePointBefore_98218a2785b3f776,
        mid_codePointBefore_4c67fb52be240c28,
        mid_codePointBefore_b92cf8f753e2d54d,
        mid_codePointCount_b92cf8f753e2d54d,
        mid_codePointCount_ac2d5951f55781e5,
        mid_compare_ceb104e6e8561784,
        mid_compareTo_ccb6ad50e04c7425,
        mid_digit_d9c0fd9859636e9e,
        mid_digit_3d7ede988f6b3a33,
        mid_equals_04e1a7382c29bc4b,
        mid_forDigit_d85a8f7c376531ab,
        mid_getDirectionality_c2f24e9c157e0376,
        mid_getDirectionality_f76f53993d2cc81b,
        mid_getName_ab09aaf2e63107e3,
        mid_getNumericValue_4b23a339ec27bbb3,
        mid_getNumericValue_5e8f8009813d7b73,
        mid_getType_5e8f8009813d7b73,
        mid_getType_4b23a339ec27bbb3,
        mid_hashCode_60df5a771df5b62d,
        mid_hashCode_5e8f8009813d7b73,
        mid_highSurrogate_bdde8923c8d84ea7,
        mid_isAlphabetic_ac5e1ea02cadda84,
        mid_isBmpCodePoint_ac5e1ea02cadda84,
        mid_isDefined_67259970fec09687,
        mid_isDefined_ac5e1ea02cadda84,
        mid_isDigit_ac5e1ea02cadda84,
        mid_isDigit_67259970fec09687,
        mid_isHighSurrogate_67259970fec09687,
        mid_isISOControl_67259970fec09687,
        mid_isISOControl_ac5e1ea02cadda84,
        mid_isIdentifierIgnorable_67259970fec09687,
        mid_isIdentifierIgnorable_ac5e1ea02cadda84,
        mid_isIdeographic_ac5e1ea02cadda84,
        mid_isJavaIdentifierPart_ac5e1ea02cadda84,
        mid_isJavaIdentifierPart_67259970fec09687,
        mid_isJavaIdentifierStart_67259970fec09687,
        mid_isJavaIdentifierStart_ac5e1ea02cadda84,
        mid_isJavaLetter_67259970fec09687,
        mid_isJavaLetterOrDigit_67259970fec09687,
        mid_isLetter_67259970fec09687,
        mid_isLetter_ac5e1ea02cadda84,
        mid_isLetterOrDigit_67259970fec09687,
        mid_isLetterOrDigit_ac5e1ea02cadda84,
        mid_isLowSurrogate_67259970fec09687,
        mid_isLowerCase_67259970fec09687,
        mid_isLowerCase_ac5e1ea02cadda84,
        mid_isMirrored_ac5e1ea02cadda84,
        mid_isMirrored_67259970fec09687,
        mid_isSpace_67259970fec09687,
        mid_isSpaceChar_67259970fec09687,
        mid_isSpaceChar_ac5e1ea02cadda84,
        mid_isSupplementaryCodePoint_ac5e1ea02cadda84,
        mid_isSurrogate_67259970fec09687,
        mid_isSurrogatePair_14ab155827503d09,
        mid_isTitleCase_67259970fec09687,
        mid_isTitleCase_ac5e1ea02cadda84,
        mid_isUnicodeIdentifierPart_ac5e1ea02cadda84,
        mid_isUnicodeIdentifierPart_67259970fec09687,
        mid_isUnicodeIdentifierStart_ac5e1ea02cadda84,
        mid_isUnicodeIdentifierStart_67259970fec09687,
        mid_isUpperCase_ac5e1ea02cadda84,
        mid_isUpperCase_67259970fec09687,
        mid_isValidCodePoint_ac5e1ea02cadda84,
        mid_isWhitespace_67259970fec09687,
        mid_isWhitespace_ac5e1ea02cadda84,
        mid_lowSurrogate_bdde8923c8d84ea7,
        mid_offsetByCodePoints_ac2d5951f55781e5,
        mid_offsetByCodePoints_45e91eb00e10c606,
        mid_reverseBytes_d1464336d7bee138,
        mid_toChars_0267698bd3da4f10,
        mid_toChars_3ac70d32bee56269,
        mid_toCodePoint_ceb104e6e8561784,
        mid_toLowerCase_4b23a339ec27bbb3,
        mid_toLowerCase_d1464336d7bee138,
        mid_toString_c041e21e63165d2d,
        mid_toString_82ceb9edccd24fa3,
        mid_toTitleCase_4b23a339ec27bbb3,
        mid_toTitleCase_d1464336d7bee138,
        mid_toUpperCase_d1464336d7bee138,
        mid_toUpperCase_4b23a339ec27bbb3,
        mid_valueOf_498158d66926f36f,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Character(jobject obj) : ::java::lang::Object(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Character(const Character& obj) : ::java::lang::Object(obj) {}

      static jint BYTES;
      static jbyte COMBINING_SPACING_MARK;
      static jbyte CONNECTOR_PUNCTUATION;
      static jbyte CONTROL;
      static jbyte CURRENCY_SYMBOL;
      static jbyte DASH_PUNCTUATION;
      static jbyte DECIMAL_DIGIT_NUMBER;
      static jbyte DIRECTIONALITY_ARABIC_NUMBER;
      static jbyte DIRECTIONALITY_BOUNDARY_NEUTRAL;
      static jbyte DIRECTIONALITY_COMMON_NUMBER_SEPARATOR;
      static jbyte DIRECTIONALITY_EUROPEAN_NUMBER;
      static jbyte DIRECTIONALITY_EUROPEAN_NUMBER_SEPARATOR;
      static jbyte DIRECTIONALITY_EUROPEAN_NUMBER_TERMINATOR;
      static jbyte DIRECTIONALITY_LEFT_TO_RIGHT;
      static jbyte DIRECTIONALITY_LEFT_TO_RIGHT_EMBEDDING;
      static jbyte DIRECTIONALITY_LEFT_TO_RIGHT_OVERRIDE;
      static jbyte DIRECTIONALITY_NONSPACING_MARK;
      static jbyte DIRECTIONALITY_OTHER_NEUTRALS;
      static jbyte DIRECTIONALITY_PARAGRAPH_SEPARATOR;
      static jbyte DIRECTIONALITY_POP_DIRECTIONAL_FORMAT;
      static jbyte DIRECTIONALITY_RIGHT_TO_LEFT;
      static jbyte DIRECTIONALITY_RIGHT_TO_LEFT_ARABIC;
      static jbyte DIRECTIONALITY_RIGHT_TO_LEFT_EMBEDDING;
      static jbyte DIRECTIONALITY_RIGHT_TO_LEFT_OVERRIDE;
      static jbyte DIRECTIONALITY_SEGMENT_SEPARATOR;
      static jbyte DIRECTIONALITY_UNDEFINED;
      static jbyte DIRECTIONALITY_WHITESPACE;
      static jbyte ENCLOSING_MARK;
      static jbyte END_PUNCTUATION;
      static jbyte FINAL_QUOTE_PUNCTUATION;
      static jbyte FORMAT;
      static jbyte INITIAL_QUOTE_PUNCTUATION;
      static jbyte LETTER_NUMBER;
      static jbyte LINE_SEPARATOR;
      static jbyte LOWERCASE_LETTER;
      static jbyte MATH_SYMBOL;
      static jint MAX_CODE_POINT;
      static jchar MAX_HIGH_SURROGATE;
      static jchar MAX_LOW_SURROGATE;
      static jint MAX_RADIX;
      static jchar MAX_SURROGATE;
      static jchar MAX_VALUE;
      static jint MIN_CODE_POINT;
      static jchar MIN_HIGH_SURROGATE;
      static jchar MIN_LOW_SURROGATE;
      static jint MIN_RADIX;
      static jint MIN_SUPPLEMENTARY_CODE_POINT;
      static jchar MIN_SURROGATE;
      static jchar MIN_VALUE;
      static jbyte MODIFIER_LETTER;
      static jbyte MODIFIER_SYMBOL;
      static jbyte NON_SPACING_MARK;
      static jbyte OTHER_LETTER;
      static jbyte OTHER_NUMBER;
      static jbyte OTHER_PUNCTUATION;
      static jbyte OTHER_SYMBOL;
      static jbyte PARAGRAPH_SEPARATOR;
      static jbyte PRIVATE_USE;
      static jint SIZE;
      static jbyte SPACE_SEPARATOR;
      static jbyte START_PUNCTUATION;
      static jbyte SURROGATE;
      static jbyte TITLECASE_LETTER;
      static ::java::lang::Class *TYPE;
      static jbyte UNASSIGNED;
      static jbyte UPPERCASE_LETTER;

      Character(jchar);

      static jint charCount(jint);
      jchar charValue() const;
      static jint codePointAt(const JArray< jchar > &, jint);
      static jint codePointAt(const ::java::lang::CharSequence &, jint);
      static jint codePointAt(const JArray< jchar > &, jint, jint);
      static jint codePointBefore(const JArray< jchar > &, jint);
      static jint codePointBefore(const ::java::lang::CharSequence &, jint);
      static jint codePointBefore(const JArray< jchar > &, jint, jint);
      static jint codePointCount(const JArray< jchar > &, jint, jint);
      static jint codePointCount(const ::java::lang::CharSequence &, jint, jint);
      static jint compare(jchar, jchar);
      jint compareTo(const Character &) const;
      static jint digit(jchar, jint);
      static jint digit(jint, jint);
      jboolean equals(const ::java::lang::Object &) const;
      static jchar forDigit(jint, jint);
      static jbyte getDirectionality(jchar);
      static jbyte getDirectionality(jint);
      static ::java::lang::String getName(jint);
      static jint getNumericValue(jint);
      static jint getNumericValue(jchar);
      static jint getType(jchar);
      static jint getType(jint);
      jint hashCode() const;
      static jint hashCode(jchar);
      static jchar highSurrogate(jint);
      static jboolean isAlphabetic(jint);
      static jboolean isBmpCodePoint(jint);
      static jboolean isDefined(jchar);
      static jboolean isDefined(jint);
      static jboolean isDigit(jint);
      static jboolean isDigit(jchar);
      static jboolean isHighSurrogate(jchar);
      static jboolean isISOControl(jchar);
      static jboolean isISOControl(jint);
      static jboolean isIdentifierIgnorable(jchar);
      static jboolean isIdentifierIgnorable(jint);
      static jboolean isIdeographic(jint);
      static jboolean isJavaIdentifierPart(jint);
      static jboolean isJavaIdentifierPart(jchar);
      static jboolean isJavaIdentifierStart(jchar);
      static jboolean isJavaIdentifierStart(jint);
      static jboolean isJavaLetter(jchar);
      static jboolean isJavaLetterOrDigit(jchar);
      static jboolean isLetter(jchar);
      static jboolean isLetter(jint);
      static jboolean isLetterOrDigit(jchar);
      static jboolean isLetterOrDigit(jint);
      static jboolean isLowSurrogate(jchar);
      static jboolean isLowerCase(jchar);
      static jboolean isLowerCase(jint);
      static jboolean isMirrored(jint);
      static jboolean isMirrored(jchar);
      static jboolean isSpace(jchar);
      static jboolean isSpaceChar(jchar);
      static jboolean isSpaceChar(jint);
      static jboolean isSupplementaryCodePoint(jint);
      static jboolean isSurrogate(jchar);
      static jboolean isSurrogatePair(jchar, jchar);
      static jboolean isTitleCase(jchar);
      static jboolean isTitleCase(jint);
      static jboolean isUnicodeIdentifierPart(jint);
      static jboolean isUnicodeIdentifierPart(jchar);
      static jboolean isUnicodeIdentifierStart(jint);
      static jboolean isUnicodeIdentifierStart(jchar);
      static jboolean isUpperCase(jint);
      static jboolean isUpperCase(jchar);
      static jboolean isValidCodePoint(jint);
      static jboolean isWhitespace(jchar);
      static jboolean isWhitespace(jint);
      static jchar lowSurrogate(jint);
      static jint offsetByCodePoints(const ::java::lang::CharSequence &, jint, jint);
      static jint offsetByCodePoints(const JArray< jchar > &, jint, jint, jint, jint);
      static jchar reverseBytes(jchar);
      static JArray< jchar > toChars(jint);
      static jint toChars(jint, const JArray< jchar > &, jint);
      static jint toCodePoint(jchar, jchar);
      static jint toLowerCase(jint);
      static jchar toLowerCase(jchar);
      ::java::lang::String toString() const;
      static ::java::lang::String toString(jchar);
      static jint toTitleCase(jint);
      static jchar toTitleCase(jchar);
      static jchar toUpperCase(jchar);
      static jint toUpperCase(jint);
      static Character valueOf(jchar);
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Character);

    class t_Character {
    public:
      PyObject_HEAD
      Character object;
      static PyObject *wrap_Object(const Character&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
