; ModuleID = '14.cpp'
source_filename = "14.cpp"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

module asm ".globl _ZSt21ios_base_library_initv"

@.str = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.str.1 = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1

; Function Attrs: mustprogress noinline norecurse optnone uwtable
define dso_local noundef i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [100 x i32], align 16
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 0, ptr %1, align 4
  %6 = call i32 (ptr, ...) @__isoc23_scanf(ptr noundef @.str, ptr noundef %5)
  store i32 0, ptr %4, align 4
  br label %7

7:                                                ; preds = %16, %0
  %8 = load i32, ptr %4, align 4
  %9 = load i32, ptr %5, align 4
  %10 = icmp slt i32 %8, %9
  br i1 %10, label %11, label %19

11:                                               ; preds = %7
  %12 = load i32, ptr %4, align 4
  %13 = sext i32 %12 to i64
  %14 = getelementptr inbounds [100 x i32], ptr %2, i64 0, i64 %13
  %15 = call i32 (ptr, ...) @__isoc23_scanf(ptr noundef @.str, ptr noundef %14)
  br label %16

16:                                               ; preds = %11
  %17 = load i32, ptr %4, align 4
  %18 = add nsw i32 %17, 1
  store i32 %18, ptr %4, align 4
  br label %7, !llvm.loop !6

19:                                               ; preds = %7
  store i32 0, ptr %4, align 4
  br label %20

20:                                               ; preds = %33, %19
  %21 = load i32, ptr %4, align 4
  %22 = load i32, ptr %5, align 4
  %23 = icmp slt i32 %21, %22
  br i1 %23, label %24, label %36

24:                                               ; preds = %20
  %25 = load i32, ptr %4, align 4
  %26 = sext i32 %25 to i64
  %27 = getelementptr inbounds [100 x i32], ptr %2, i64 0, i64 %26
  %28 = load i32, ptr %27, align 4
  %29 = call noundef i32 @_Z1fii(i32 noundef 1, i32 noundef %28)
  %30 = add nsw i32 %29, 1
  store i32 %30, ptr %3, align 4
  %31 = load i32, ptr %3, align 4
  %32 = call i32 (ptr, ...) @printf(ptr noundef @.str.1, i32 noundef %31)
  br label %33

33:                                               ; preds = %24
  %34 = load i32, ptr %4, align 4
  %35 = add nsw i32 %34, 1
  store i32 %35, ptr %4, align 4
  br label %20, !llvm.loop !8

36:                                               ; preds = %20
  ret i32 0
}

declare i32 @__isoc23_scanf(ptr noundef, ...) #1

; Function Attrs: mustprogress noinline optnone uwtable
define dso_local noundef i32 @_Z1fii(i32 noundef %0, i32 noundef %1) #2 {
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  store i32 %0, ptr %3, align 4
  store i32 %1, ptr %4, align 4
  store i32 0, ptr %7, align 4
  %8 = load i32, ptr %3, align 4
  store i32 %8, ptr %5, align 4
  br label %9

9:                                                ; preds = %46, %2
  %10 = load i32, ptr %5, align 4
  %11 = load i32, ptr %4, align 4
  %12 = sitofp i32 %11 to double
  %13 = call double @sqrt(double noundef %12) #4
  %14 = fptosi double %13 to i32
  %15 = add nsw i32 %14, 1
  %16 = icmp slt i32 %10, %15
  br i1 %16, label %17, label %49

17:                                               ; preds = %9
  %18 = load i32, ptr %7, align 4
  store i32 %18, ptr %6, align 4
  %19 = load i32, ptr %5, align 4
  %20 = icmp eq i32 %19, 1
  br i1 %20, label %21, label %22

21:                                               ; preds = %17
  store i32 0, ptr %7, align 4
  br label %42

22:                                               ; preds = %17
  %23 = load i32, ptr %4, align 4
  %24 = load i32, ptr %5, align 4
  %25 = srem i32 %23, %24
  %26 = icmp eq i32 %25, 0
  br i1 %26, label %27, label %40

27:                                               ; preds = %22
  %28 = load i32, ptr %4, align 4
  %29 = load i32, ptr %5, align 4
  %30 = sdiv i32 %28, %29
  %31 = load i32, ptr %5, align 4
  %32 = icmp sge i32 %30, %31
  br i1 %32, label %33, label %40

33:                                               ; preds = %27
  %34 = load i32, ptr %5, align 4
  %35 = load i32, ptr %4, align 4
  %36 = load i32, ptr %5, align 4
  %37 = sdiv i32 %35, %36
  %38 = call noundef i32 @_Z1fii(i32 noundef %34, i32 noundef %37)
  %39 = add nsw i32 %38, 1
  store i32 %39, ptr %7, align 4
  br label %41

40:                                               ; preds = %27, %22
  store i32 0, ptr %7, align 4
  br label %41

41:                                               ; preds = %40, %33
  br label %42

42:                                               ; preds = %41, %21
  %43 = load i32, ptr %7, align 4
  %44 = load i32, ptr %6, align 4
  %45 = add nsw i32 %43, %44
  store i32 %45, ptr %7, align 4
  br label %46

46:                                               ; preds = %42
  %47 = load i32, ptr %5, align 4
  %48 = add nsw i32 %47, 1
  store i32 %48, ptr %5, align 4
  br label %9, !llvm.loop !9

49:                                               ; preds = %9
  %50 = load i32, ptr %7, align 4
  ret i32 %50
}

declare i32 @printf(ptr noundef, ...) #1

; Function Attrs: nounwind
declare double @sqrt(double noundef) #3

attributes #0 = { mustprogress noinline norecurse optnone uwtable "frame-pointer"="all" "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { "frame-pointer"="all" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { mustprogress noinline optnone uwtable "frame-pointer"="all" "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nounwind "frame-pointer"="all" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3, !4}
!llvm.ident = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{i32 7, !"frame-pointer", i32 2}
!5 = !{!"Ubuntu clang version 18.1.3 (1ubuntu1)"}
!6 = distinct !{!6, !7}
!7 = !{!"llvm.loop.mustprogress"}
!8 = distinct !{!8, !7}
!9 = distinct !{!9, !7}
