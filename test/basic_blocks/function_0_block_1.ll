None:

8:                                                ; preds = %36, %0
%9 = load i32, ptr %3, align 4
%10 = load i32, ptr %5, align 4
%11 = icmp sle i32 %9, %10
br i1 %11, label %12, label %39
