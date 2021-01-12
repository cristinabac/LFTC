/* A Bison parser, made by GNU Bison 3.5.1.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

#ifndef YY_YY_PARSER_TAB_H_INCLUDED
# define YY_YY_PARSER_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    ID = 258,
    CONSTANT = 259,
    CRESTE_VALOAREA = 260,
    PRIMESTE = 261,
    EGALITE_FRATERNITE = 262,
    OARE = 263,
    NUP = 264,
    NUMAR_INTREG = 265,
    DA_LA_PC = 266,
    ARATA = 267,
    PARCURGE = 268,
    SIR = 269,
    DE = 270,
    CARACTER = 271,
    COLON = 272,
    SEMI_COLON = 273,
    COMA = 274,
    DOT = 275,
    MINUS = 276,
    MULTIPLY = 277,
    DIVISION = 278,
    MODULO = 279,
    LEFT_ROUND_PARENTHESIS = 280,
    RIGHT_ROUND_PARENTHESIS = 281,
    LEFT_SQUARE_PARENTHESIS = 282,
    RIGHT_SQUARE_PARENTHESIS = 283,
    LEFT_ACOLADE = 284,
    RIGHT_ACOLADE = 285,
    LESS_THAN = 286,
    GREATER_THAN = 287,
    LESS_OR_EQUAL_THAN = 288,
    GREATER_OR_EQUAL_THAN = 289,
    IN_OPERATOR = 290,
    OUT_OPERATOR = 291
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_PARSER_TAB_H_INCLUDED  */
