None:

30:                                               ; preds = %29
%31 = load i32, ptr %4, align 4
%32 = add nsw i32 %31, 1
store i32 %32, ptr %4, align 4
br label %14, !llvm.loop !6
