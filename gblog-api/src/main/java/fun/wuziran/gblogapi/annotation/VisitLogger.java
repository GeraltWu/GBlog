package fun.wuziran.gblogapi.annotation;

import fun.wuziran.gblogapi.enums.VisitBehavior;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * @Description 用于记录访问日志的注解
 * @Author Geralt
 * @Date 2024/7/17
 */

@Target(ElementType.METHOD) //ElementType.METHOD表示这个方法注解只能应用于方法
@Retention(RetentionPolicy.RUNTIME) //RetentionPolicy.RUNTIME表示这个注解在运行时也有效，可以通过反射机制获取到
public @interface VisitLogger {
    /**
     * 返回行为枚举，value方法（默认方法）
     * @return 一个VisitBehavior枚举类型的变量，默认返回 VisitBehavior 枚举类型中的 UNKNOWN 枚举对象
     */
    VisitBehavior value() default VisitBehavior.UNKNOWN;
}

