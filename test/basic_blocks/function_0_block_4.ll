None:

18:                                               ; preds = %14
%19 = load i32, ptr %2, align 4
%20 = load i32, ptr %4, align 4
%21 = srem i32 %19, %20
%22 = icmp eq i32 %21, 0
br i1 %22, label %23, label %29
