None:
define dso_local noundef i32 @_Z1fii(i32 noundef %0, i32 noundef %1) #2 {
%3 = alloca i32, align 4
%4 = alloca i32, align 4
%5 = alloca i32, align 4
%6 = alloca i32, align 4
store i32 %0, ptr %3, align 4
store i32 %1, ptr %4, align 4
store i32 0, ptr %6, align 4
%7 = load i32, ptr %4, align 4
%8 = load i32, ptr %3, align 4
%9 = icmp eq i32 %7, %8
br i1 %9, label %10, label %11
