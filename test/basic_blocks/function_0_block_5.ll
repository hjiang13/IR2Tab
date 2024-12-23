None:

23:                                               ; preds = %18
%24 = load i32, ptr %2, align 4
%25 = load i32, ptr %4, align 4
%26 = call noundef i32 @_Z1fii(i32 noundef %24, i32 noundef %25)
%27 = load i32, ptr %6, align 4
%28 = add nsw i32 %27, %26
store i32 %28, ptr %6, align 4
br label %29
