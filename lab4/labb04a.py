def split_rec(indata):
    word_left = ""
    word_right = ""
    if not indata:
        return word_left, word_right
    word_left, word_right = split_rec(indata[1:]) 
    if indata[0].islower() or indata[0] == "_" or indata[0] == ".":
        word_left = indata[0] + word_left
    elif indata[0].isupper() or indata[0] == "|" or indata[0] == " ":
        word_right = indata[0] + word_right
    return word_left, word_right

def split_it(indata, word_left = "", word_right = ""):
    for c in indata:
        if c.islower() or c == "_" or c == ".":
            word_left += c
        if c.isupper() or c == "|" or c == " ":
            word_right += c
    return word_left, word_right
        


print(split_rec("WhEa'n<=R_´Ek o§Nm&O_,7 s!So1TmR_%Ae%Nt#@GtE_/Ry`2Sr>! v*;Tä>Od<< eLr44O_Ve0En)|_/+ a6YpOrUi/& lKa9Nf§Ot<Wo$ n1*T_8Ho`7Ec/= hR_?0Uh0La8<EdSe32 _`1Ae%0Nt*Dt _35ShOö2 gDaOn ä,Is|k rAu; s>$F_7UiL_@Le8 n&C_`%Os;Mv6+Må2In+Tg<<Mr=5Ee,Nm+T_&'oSm _0(Wh#HaAl*5Ts e5In5'.M_`? c&>Tl,Ha@5IrNa9(K_Io#$Nc$?Gh5 _5?OlFo!|t tYeOnU_? vWoOr(´Uo34L_)Di>Nn(3'n6@Te?> _=Gm#2Ee;Td§$ _7Ts,HkIö>St! e#Fk3Ra0On=M_ a%At!)Nt!8Y_? hOäTm%1Ht74Ea+R_8; hGo=Un-*Yo)|m´& _<§Ip&4 åJ_UdSa=´Tl% a-+Wr)AöN_Nb=5Ar yTg)Eg4LaL; _Ym7Oe&Un _3§Hd/Oe%8Wt5 _Id-3'r=/Mö j?!FdEe1E_Le73IvNiGg?1|h<% e´(Gt@*Oe,Tr%T,A_ iMn6An`§Ka2En3! _47Yd5´OeU_ k@Uo-NmDmEo%R_SiT_&<Ab)NåDt69|."))