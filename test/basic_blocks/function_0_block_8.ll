None:

33:                                               ; preds = %14
%34 = load i32, ptr %6, align 4
%35 = call i32 (ptr, ...) @printf(ptr noundef @.str.1, i32 noundef %34)
store i32 0, ptr %6, align 4
br label %36
