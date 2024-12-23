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

8:                                                ; preds = %36, %0
%9 = load i32, ptr %3, align 4
%10 = load i32, ptr %5, align 4
%11 = icmp sle i32 %9, %10
br i1 %11, label %12, label %39

12:                                               ; preds = %8
%13 = call i32 (ptr, ...) @__isoc23_scanf(ptr noundef @.str, ptr noundef %2)
store i32 2, ptr %4, align 4
br label %14

14:                                               ; preds = %30, %12
%15 = load i32, ptr %4, align 4
%16 = load i32, ptr %2, align 4
%17 = icmp sle i32 %15, %16
br i1 %17, label %18, label %33

18:                                               ; preds = %14
%19 = load i32, ptr %2, align 4
%20 = load i32, ptr %4, align 4
%21 = srem i32 %19, %20
%22 = icmp eq i32 %21, 0
br i1 %22, label %23, label %29

23:                                               ; preds = %18
%24 = load i32, ptr %2, align 4
%25 = load i32, ptr %4, align 4
%26 = call noundef i32 @_Z1fii(i32 noundef %24, i32 noundef %25)
%27 = load i32, ptr %6, align 4
%28 = add nsw i32 %27, %26
store i32 %28, ptr %6, align 4
br label %29

29:                                               ; preds = %23, %18
br label %30

30:                                               ; preds = %29
%31 = load i32, ptr %4, align 4
%32 = add nsw i32 %31, 1
store i32 %32, ptr %4, align 4
br label %14, !llvm.loop !6

33:                                               ; preds = %14
%34 = load i32, ptr %6, align 4
%35 = call i32 (ptr, ...) @printf(ptr noundef @.str.1, i32 noundef %34)
store i32 0, ptr %6, align 4
br label %36

36:                                               ; preds = %33
%37 = load i32, ptr %3, align 4
%38 = add nsw i32 %37, 1
store i32 %38, ptr %3, align 4
br label %8, !llvm.loop !8

39:                                               ; preds = %8
ret i32 0
}
