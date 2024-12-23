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

10:                                               ; preds = %2
store i32 1, ptr %6, align 4
br label %36

11:                                               ; preds = %2
%12 = load i32, ptr %3, align 4
%13 = load i32, ptr %4, align 4
%14 = sdiv i32 %12, %13
store i32 %14, ptr %3, align 4
%15 = load i32, ptr %4, align 4
store i32 %15, ptr %5, align 4
br label %16

16:                                               ; preds = %32, %11
%17 = load i32, ptr %5, align 4
%18 = load i32, ptr %3, align 4
%19 = icmp sle i32 %17, %18
br i1 %19, label %20, label %35

20:                                               ; preds = %16
%21 = load i32, ptr %3, align 4
%22 = load i32, ptr %5, align 4
%23 = srem i32 %21, %22
%24 = icmp eq i32 %23, 0
br i1 %24, label %25, label %31

25:                                               ; preds = %20
%26 = load i32, ptr %3, align 4
%27 = load i32, ptr %5, align 4
%28 = call noundef i32 @_Z1fii(i32 noundef %26, i32 noundef %27)
%29 = load i32, ptr %6, align 4
%30 = add nsw i32 %29, %28
store i32 %30, ptr %6, align 4
br label %31

31:                                               ; preds = %25, %20
br label %32

32:                                               ; preds = %31
%33 = load i32, ptr %5, align 4
%34 = add nsw i32 %33, 1
store i32 %34, ptr %5, align 4
br label %16, !llvm.loop !9

35:                                               ; preds = %16
br label %36

36:                                               ; preds = %35, %10
%37 = load i32, ptr %6, align 4
ret i32 %37
}
