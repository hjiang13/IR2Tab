None:

32:                                               ; preds = %31
%33 = load i32, ptr %5, align 4
%34 = add nsw i32 %33, 1
store i32 %34, ptr %5, align 4
br label %16, !llvm.loop !9
