# Generated from C:/Users/Leo/IdeaProjects/compilerbau/grammar\SPL.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SPLParser import SPLParser
else:
    from SPLParser import SPLParser

# This class defines a complete listener for a parse tree produced by SPLParser.
class SPLListener(ParseTreeListener):

    # Enter a parse tree produced by SPLParser#program.
    def enterProgram(self, ctx:SPLParser.ProgramContext):
        pass

    # Exit a parse tree produced by SPLParser#program.
    def exitProgram(self, ctx:SPLParser.ProgramContext):
        pass


    # Enter a parse tree produced by SPLParser#declaration.
    def enterDeclaration(self, ctx:SPLParser.DeclarationContext):
        pass

    # Exit a parse tree produced by SPLParser#declaration.
    def exitDeclaration(self, ctx:SPLParser.DeclarationContext):
        pass


    # Enter a parse tree produced by SPLParser#varDecl.
    def enterVarDecl(self, ctx:SPLParser.VarDeclContext):
        pass

    # Exit a parse tree produced by SPLParser#varDecl.
    def exitVarDecl(self, ctx:SPLParser.VarDeclContext):
        pass


    # Enter a parse tree produced by SPLParser#statement.
    def enterStatement(self, ctx:SPLParser.StatementContext):
        pass

    # Exit a parse tree produced by SPLParser#statement.
    def exitStatement(self, ctx:SPLParser.StatementContext):
        pass


    # Enter a parse tree produced by SPLParser#exprStmt.
    def enterExprStmt(self, ctx:SPLParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by SPLParser#exprStmt.
    def exitExprStmt(self, ctx:SPLParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by SPLParser#ifStmt.
    def enterIfStmt(self, ctx:SPLParser.IfStmtContext):
        pass

    # Exit a parse tree produced by SPLParser#ifStmt.
    def exitIfStmt(self, ctx:SPLParser.IfStmtContext):
        pass


    # Enter a parse tree produced by SPLParser#printStmt.
    def enterPrintStmt(self, ctx:SPLParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by SPLParser#printStmt.
    def exitPrintStmt(self, ctx:SPLParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by SPLParser#whileStmt.
    def enterWhileStmt(self, ctx:SPLParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by SPLParser#whileStmt.
    def exitWhileStmt(self, ctx:SPLParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by SPLParser#block.
    def enterBlock(self, ctx:SPLParser.BlockContext):
        pass

    # Exit a parse tree produced by SPLParser#block.
    def exitBlock(self, ctx:SPLParser.BlockContext):
        pass


    # Enter a parse tree produced by SPLParser#expression.
    def enterExpression(self, ctx:SPLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SPLParser#expression.
    def exitExpression(self, ctx:SPLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SPLParser#assignment.
    def enterAssignment(self, ctx:SPLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SPLParser#assignment.
    def exitAssignment(self, ctx:SPLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SPLParser#logic_or.
    def enterLogic_or(self, ctx:SPLParser.Logic_orContext):
        pass

    # Exit a parse tree produced by SPLParser#logic_or.
    def exitLogic_or(self, ctx:SPLParser.Logic_orContext):
        pass


    # Enter a parse tree produced by SPLParser#logic_and.
    def enterLogic_and(self, ctx:SPLParser.Logic_andContext):
        pass

    # Exit a parse tree produced by SPLParser#logic_and.
    def exitLogic_and(self, ctx:SPLParser.Logic_andContext):
        pass


    # Enter a parse tree produced by SPLParser#equality.
    def enterEquality(self, ctx:SPLParser.EqualityContext):
        pass

    # Exit a parse tree produced by SPLParser#equality.
    def exitEquality(self, ctx:SPLParser.EqualityContext):
        pass


    # Enter a parse tree produced by SPLParser#comparison.
    def enterComparison(self, ctx:SPLParser.ComparisonContext):
        pass

    # Exit a parse tree produced by SPLParser#comparison.
    def exitComparison(self, ctx:SPLParser.ComparisonContext):
        pass


    # Enter a parse tree produced by SPLParser#term.
    def enterTerm(self, ctx:SPLParser.TermContext):
        pass

    # Exit a parse tree produced by SPLParser#term.
    def exitTerm(self, ctx:SPLParser.TermContext):
        pass


    # Enter a parse tree produced by SPLParser#factor.
    def enterFactor(self, ctx:SPLParser.FactorContext):
        pass

    # Exit a parse tree produced by SPLParser#factor.
    def exitFactor(self, ctx:SPLParser.FactorContext):
        pass


    # Enter a parse tree produced by SPLParser#unary.
    def enterUnary(self, ctx:SPLParser.UnaryContext):
        pass

    # Exit a parse tree produced by SPLParser#unary.
    def exitUnary(self, ctx:SPLParser.UnaryContext):
        pass


    # Enter a parse tree produced by SPLParser#primary.
    def enterPrimary(self, ctx:SPLParser.PrimaryContext):
        pass

    # Exit a parse tree produced by SPLParser#primary.
    def exitPrimary(self, ctx:SPLParser.PrimaryContext):
        pass



del SPLParser