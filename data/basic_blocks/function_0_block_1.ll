None:

; <label>:12:                                     ; preds = %2
%13 = tail call i64 @_Z15get_global_sizej(i32 1) #3
%14 = trunc i64 %13 to i32
%15 = add i32 %8, -1
%16 = icmp ugt i32 %15, %4
%17 = icmp ne i32 %6, 0
%18 = and i1 %17, %16
%19 = add i32 %14, -1
%20 = icmp ugt i32 %19, %6
%21 = and i1 %18, %20
br i1 %21, label %22, label %87
