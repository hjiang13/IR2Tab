None:

11:                                               ; preds = %2
%12 = load i32, ptr %3, align 4
%13 = load i32, ptr %4, align 4
%14 = sdiv i32 %12, %13
store i32 %14, ptr %3, align 4
%15 = load i32, ptr %4, align 4
store i32 %15, ptr %5, align 4
br label %16
