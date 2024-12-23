None:

20:                                               ; preds = %16
%21 = load i32, ptr %3, align 4
%22 = load i32, ptr %5, align 4
%23 = srem i32 %21, %22
%24 = icmp eq i32 %23, 0
br i1 %24, label %25, label %31
