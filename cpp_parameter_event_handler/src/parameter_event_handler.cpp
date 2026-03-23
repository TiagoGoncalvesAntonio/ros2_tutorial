// The first statement, #include <memory> is included so that the code can utilize the std::make_shared template.
#include <memory>

// #include "rclcpp/rclcpp.hpp" is included to allow the code to reference the various functionality provided by 
// the rclcpp interface, including the ParameterEventHandler class
#include "rclcpp/rclcpp.hpp"

// After the class declaration, the code defines a class, SampleNodeWithParameters
class SampleNodeWithParameters : public rclcpp::Node
{
public:
    SampleNodeWithParameters()
    : Node("node_with_parameters")
    {
        // The constructor for the class declares an integer parameter an_int_param, with a default value of 0.
        this->declare_parameter("an_int_param", 0);

        // Create a parameter subscriber that can be used to monitor parameter changes
        // (for this node's parameters as well as other nodes' parameters)
        param_subscriber_ = std::make_shared<rclcpp::ParameterEventHandler>(this);

        // the code creates a lambda function and sets it as the callback to invoke whenever an_int_param is updated.
        // Set a callback for this node's integer parameter, "an_int_param"
        auto cb = [this](const rclcpp::Parameter & p) {
            RCLCPP_INFO(
            this->get_logger(), "cb: Received an update to parameter \"%s\" of type %s: \"%ld\"",
            p.get_name().c_str(),
            p.get_type_name().c_str(),
            p.as_int());
        };
        // It is very important to save the handle that is returned by add_parameter_callback; otherwise, 
        // The callback will not be properly registered.
        cb_handle_ = param_subscriber_->add_parameter_callback("an_int_param", cb);

        // Now, add a callback to monitor any changes to the remote node's parameter. In this
        // case, we supply the remote node name.
        auto cb2 = [this](const rclcpp::Parameter & p) {
            RCLCPP_INFO(
            this->get_logger(), "cb2: Received an update to parameter \"%s\" of type: %s: \"%.02lf\"",
            p.get_name().c_str(),
            p.get_type_name().c_str(),
            p.as_double());
        };
        auto remote_node_name = std::string("parameter_blackboard");
        auto remote_param_name = std::string("a_double_param");
        cb_handle2_ = param_subscriber_->add_parameter_callback(remote_param_name, cb2, remote_node_name);
    }

private:
    std::shared_ptr<rclcpp::ParameterEventHandler> param_subscriber_;
    std::shared_ptr<rclcpp::ParameterCallbackHandle> cb_handle_;
    // 
    std::shared_ptr<rclcpp::ParameterCallbackHandle> cb_handle2_;  // Add this
};

// Following the SampleNodeWithParameters is a typical main function which initializes ROS, spins 
// the sample node so that it can send and receive messages, and then shuts down after the user enters ^C at the console.
int main(int argc, char ** argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<SampleNodeWithParameters>());
    rclcpp::shutdown();

    return 0;
}