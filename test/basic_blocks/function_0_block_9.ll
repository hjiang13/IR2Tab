None:

36:                                               ; preds = %33
%37 = load i32, ptr %3, align 4
%38 = add nsw i32 %37, 1
store i32 %38, ptr %3, align 4
br label %8, !llvm.loop !8
