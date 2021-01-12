%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1
%}

%token ID
%token CONSTANT
%token CRESTE_VALOAREA
%token PRIMESTE
%token EGALITE_FRATERNITE
%token OARE
%token NUP
%token NUMAR_INTREG
%token DA_LA_PC
%token ARATA
%token PARCURGE
%token SIR
%token DE
%token CARACTER
%token COLON
%token SEMI_COLON
%token COMA
%token DOT
%token MINUS
%token MULTIPLY
%token DIVISION
%token MODULO
%token LEFT_ROUND_PARENTHESIS
%token RIGHT_ROUND_PARENTHESIS
%token LEFT_SQUARE_PARENTHESIS
%token RIGHT_SQUARE_PARENTHESIS
%token LEFT_ACOLADE
%token RIGHT_ACOLADE
%token LESS_THAN
%token GREATER_THAN
%token LESS_OR_EQUAL_THAN
%token GREATER_OR_EQUAL_THAN
%token IN_OPERATOR
%token OUT_OPERATOR

%left CRESTE_VALOAREA MINUS
%left MULTIPLY DIVISION MODULO

%start program

%%

program: StmtList {printf("1\n");} ; 

StmtList: Stmt StmtList {printf("2 \n");}
        | Stmt {printf("3 \n");} ;

Stmt: Decl {printf("4 \n");}
    | Ifstmt {printf("5 \n");}
    | Assignstmt {printf("6 \n");}
    | Iostmt {printf("7 \n");}
    | Forstmt {printf("8 \n");} ;

Decl: DType ID SEMI_COLON {printf("9 \n");}
    | DType Decl2 {printf("10 \n");} ;

DType: NUMAR_INTREG {printf("11 \n");}
     | CARACTER {printf("12 \n");}
     | NUMAR_INTREG SIR DE CONSTANT {printf("13 ");}
     | CARACTER SIR DE CONSTANT {printf("14 \n");} ;

Decl2: ID SEMI_COLON {printf("15 \n");}
     | Assignstmt2 SEMI_COLON {printf("16 \n");}
     | ID COMA Decl2 {printf("17 \n");}
     | Assignstmt2 COMA Decl2 {printf("18 \n");} ;

Ifstmt: OARE LEFT_ROUND_PARENTHESIS Condition RIGHT_ROUND_PARENTHESIS LEFT_ACOLADE StmtList RIGHT_ACOLADE NUP LEFT_ACOLADE StmtList RIGHT_ACOLADE {printf("19 \n");}
      | OARE LEFT_ROUND_PARENTHESIS Condition RIGHT_ROUND_PARENTHESIS Stmt NUP LEFT_ACOLADE StmtList RIGHT_ACOLADE {printf("20 \n");}
      | OARE LEFT_ROUND_PARENTHESIS Condition RIGHT_ROUND_PARENTHESIS LEFT_ACOLADE StmtList RIGHT_ACOLADE NUP Stmt {printf("21 \n");}
      | OARE LEFT_ROUND_PARENTHESIS Condition RIGHT_ROUND_PARENTHESIS Stmt NUP Stmt {printf("22 \n");}
      | OARE LEFT_ROUND_PARENTHESIS Condition RIGHT_ROUND_PARENTHESIS LEFT_ACOLADE StmtList RIGHT_ACOLADE {printf("23 \n");}
      | OARE LEFT_ROUND_PARENTHESIS Condition RIGHT_ROUND_PARENTHESIS Stmt {printf("24 \n");} ;


Condition: Expression Relation Expression {printf("25 \n");} ;

Relation: LESS_THAN {printf("26 \n");}
        | LESS_OR_EQUAL_THAN {printf("27 \n");}
        | EGALITE_FRATERNITE {printf("28 \n");}
        | GREATER_OR_EQUAL_THAN {printf("29 \n");}
        | GREATER_THAN {printf("30 \n");};

Forstmt: PARCURGE ForCond ForBody {printf("31 \n");};

ForCond: LEFT_ROUND_PARENTHESIS Assignstmt3 SEMI_COLON Condition SEMI_COLON Assignstmt2 RIGHT_ROUND_PARENTHESIS {printf("32 \n");};

ForBody: LEFT_ACOLADE StmtList RIGHT_ACOLADE {printf("33 \n");}
       | Stmt {printf("34 \n");} ;

Assignstmt: ID PRIMESTE Expression SEMI_COLON {printf("35 \n");} ;

Assignstmt2: ID PRIMESTE Expression {printf("36 \n");};

Assignstmt3: ID PRIMESTE Expression {printf("37 \n");}
           | NUMAR_INTREG ID PRIMESTE Expression {printf("38 \n");} ;

Iostmt: DA_LA_PC IN_OPERATOR ID SEMI_COLON {printf("39 \n");}
      | ARATA OUT_OPERATOR ID SEMI_COLON {printf("40 \n");}
      | ARATA OUT_OPERATOR CONSTANT SEMI_COLON {printf("41 \n");} ;

Expression: ArithmExpr {printf("42 \n");};

ArithmExpr : term {printf("43 \n");}
           | term CRESTE_VALOAREA ArithmExpr {printf("44 \n");}
           | term MINUS ArithmExpr {printf("45 \n");}
           | term MULTIPLY ArithmExpr {printf("46 \n");}
           | term DIVISION ArithmExpr {printf("47 \n");} 
           | term MODULO ArithmExpr {printf("48 \n");}
           | LEFT_ROUND_PARENTHESIS ArithmExpr RIGHT_ROUND_PARENTHESIS {printf("49 \n");} ;

term : ID {printf("50 \n");}
     | CONSTANT {printf("51 \n");};    


%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if (argc > 1) 
    yyin = fopen(argv[1], "r");
  if ( (argc > 2) && ( !strcmp(argv[2], "-d") ) ) 
    yydebug = 1;
  if ( !yyparse() ) 
    fprintf(stderr,"\tSuccessful\n");
}
