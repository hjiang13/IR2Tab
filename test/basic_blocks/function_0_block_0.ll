None:
define dso_local noundef i32 @main() #0 {
%1 = alloca i32, align 4
%2 = alloca i32, align 4
%3 = alloca i32, align 4
%4 = alloca i32, align 4
%5 = alloca i32, align 4
%6 = alloca i32, align 4
store i32 0, ptr %1, align 4
store i32 0, ptr %6, align 4
%7 = call i32 (ptr, ...) @__isoc23_scanf(ptr noundef @.str, ptr noundef %5)
store i32 1, ptr %3, align 4
br label %8
