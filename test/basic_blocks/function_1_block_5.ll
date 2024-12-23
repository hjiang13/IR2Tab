None:

25:                                               ; preds = %20
%26 = load i32, ptr %3, align 4
%27 = load i32, ptr %5, align 4
%28 = call noundef i32 @_Z1fii(i32 noundef %26, i32 noundef %27)
%29 = load i32, ptr %6, align 4
%30 = add nsw i32 %29, %28
store i32 %30, ptr %6, align 4
br label %31
